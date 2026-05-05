#!/usr/bin/env python3
"""Small Home Assistant add-on web server for OpenPool.

The add-on serves the static OpenPool UI and proxies selected Home Assistant
Core API calls. Supervisor authentication is preferred; a configured long-lived
access token is used as a fallback for installations where the Supervisor token
is not injected into the add-on environment.
"""

from __future__ import annotations

import json
import mimetypes
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urlparse
from urllib.request import Request, urlopen


PORT = int(os.environ.get("OPENPOOL_PORT", "8099"))
WWW_ROOT = Path(os.environ.get("OPENPOOL_WWW", "/app/www")).resolve()
OPTIONS_PATH = Path("/data/options.json")
SUPERVISOR_HA_API_BASE = "http://supervisor/core/api"
DEFAULT_HA_URL = "http://homeassistant:8123"
SUPERVISOR_TOKEN = os.environ.get("SUPERVISOR_TOKEN") or os.environ.get("HASSIO_TOKEN") or ""


class OpenPoolHandler(BaseHTTPRequestHandler):
    server_version = "OpenPool/0.1.5"

    def do_GET(self) -> None:
        parsed = urlparse(self.path)

        if parsed.path == "/healthz":
            self._send_json({"ok": True})
            return

        if parsed.path == "/api/config":
            self._send_json(self._read_public_options())
            return

        if parsed.path.startswith("/api/ha/states/"):
            entity_id = unquote(parsed.path.removeprefix("/api/ha/states/"))
            self._proxy_ha("GET", f"/states/{quote(entity_id, safe='')}")
            return

        self._serve_static(parsed.path)

    def do_POST(self) -> None:
        parsed = urlparse(self.path)

        if parsed.path.startswith("/api/ha/services/"):
            service_path = parsed.path.removeprefix("/api/ha/services/")
            self._proxy_ha("POST", f"/services/{service_path}", self._read_body())
            return

        self._send_json({"error": "Not found"}, status=404)

    def _read_options(self) -> dict:
        if not OPTIONS_PATH.exists():
            return {}

        try:
            return json.loads(OPTIONS_PATH.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {}

    def _read_body(self) -> bytes:
        length = int(self.headers.get("content-length", "0"))
        return self.rfile.read(length) if length else b"{}"

    def _read_public_options(self) -> dict:
        options = json.loads(json.dumps(self._read_options()))
        connection = options.get("connection")

        if isinstance(connection, dict):
            access_token = str(connection.get("access_token") or "").strip()
            connection["access_token"] = ""
            connection["access_token_configured"] = bool(access_token)

        return options

    def _ha_api_credentials(self) -> tuple[str, str, str] | None:
        if SUPERVISOR_TOKEN:
            return SUPERVISOR_HA_API_BASE, SUPERVISOR_TOKEN, "supervisor"

        connection = self._read_options().get("connection") or {}
        access_token = str(connection.get("access_token") or "").strip()
        if not access_token:
            return None

        homeassistant_url = str(connection.get("homeassistant_url") or DEFAULT_HA_URL).rstrip("/")
        return f"{homeassistant_url}/api", access_token, "configured_token"

    def _proxy_ha(self, method: str, path: str, body: bytes | None = None) -> None:
        credentials = self._ha_api_credentials()
        if not credentials:
            self._send_json(
                {
                    "error": "Home Assistant authentication is not configured",
                    "detail": "SUPERVISOR_TOKEN is missing and no fallback access token is configured.",
                },
                status=503,
            )
            return

        api_base, token, auth_source = credentials
        target_url = f"{api_base}{path}"
        print(f"[openpool] HA {method} {path} via {auth_source}", flush=True)
        request = Request(
            target_url,
            data=body,
            method=method,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
        )

        try:
            with urlopen(request, timeout=10) as response:
                payload = response.read()
                print(f"[openpool] HA {method} {path} -> {response.status}", flush=True)
                self.send_response(response.status)
                self.send_header("Content-Type", response.headers.get("Content-Type", "application/json"))
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)
        except HTTPError as err:
            error_payload = err.read()
            detail = error_payload.decode("utf-8", "replace")[:220] if error_payload else err.reason
            print(f"[openpool] HA {method} {path} -> {err.code}: {detail}", flush=True)
            if error_payload:
                self.send_response(err.code)
                self.send_header("Content-Type", err.headers.get("Content-Type", "application/json"))
                self.send_header("Content-Length", str(len(error_payload)))
                self.end_headers()
                self.wfile.write(error_payload)
                return

            self._send_json({"error": err.reason}, status=err.code)
        except URLError as err:
            print(f"[openpool] HA {method} {path} -> 502: {err.reason}", flush=True)
            self._send_json({"error": str(err.reason)}, status=502)

    def _serve_static(self, request_path: str) -> None:
        relative = request_path.lstrip("/") or "index.html"
        target = (WWW_ROOT / relative).resolve()

        if not str(target).startswith(str(WWW_ROOT)) or not target.exists() or target.is_dir():
            target = WWW_ROOT / "index.html"

        content_type = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
        payload = target.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        if target.name == "index.html":
            self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def _send_json(self, data: dict, status: int = 200) -> None:
        payload = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, fmt: str, *args: object) -> None:
        print(f"[openpool] {self.address_string()} - {fmt % args}", flush=True)


def main() -> None:
    server = ThreadingHTTPServer(("0.0.0.0", PORT), OpenPoolHandler)
    print(f"[openpool] listening on 0.0.0.0:{PORT}", flush=True)
    print(f"[openpool] Home Assistant auth: {_startup_auth_status()}", flush=True)
    server.serve_forever()


def _startup_auth_status() -> str:
    if SUPERVISOR_TOKEN:
        return "Supervisor token available"

    options = {}
    if OPTIONS_PATH.exists():
        try:
            options = json.loads(OPTIONS_PATH.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            options = {}

    connection = options.get("connection") or {}
    if str(connection.get("access_token") or "").strip():
        return "using configured fallback token"

    return "missing token"


if __name__ == "__main__":
    main()
