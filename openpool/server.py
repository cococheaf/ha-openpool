#!/usr/bin/env python3
"""Small Home Assistant add-on web server for OpenPool.

The add-on currently serves the static OpenPool UI and provides a minimal
Home Assistant API proxy. The proxy keeps the browser from needing a long-lived
token; it uses the Supervisor token that Home Assistant provides to add-ons.
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
HA_API_BASE = "http://supervisor/core/api"
SUPERVISOR_TOKEN = os.environ.get("SUPERVISOR_TOKEN", "")


class OpenPoolHandler(BaseHTTPRequestHandler):
    server_version = "OpenPool/0.1.2"

    def do_GET(self) -> None:
        parsed = urlparse(self.path)

        if parsed.path == "/healthz":
            self._send_json({"ok": True})
            return

        if parsed.path == "/api/config":
            self._send_json(self._read_options())
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

    def _proxy_ha(self, method: str, path: str, body: bytes | None = None) -> None:
        if not SUPERVISOR_TOKEN:
            self._send_json({"error": "SUPERVISOR_TOKEN is not available"}, status=503)
            return

        request = Request(
            f"{HA_API_BASE}{path}",
            data=body,
            method=method,
            headers={
                "Authorization": f"Bearer {SUPERVISOR_TOKEN}",
                "Content-Type": "application/json",
            },
        )

        try:
            with urlopen(request, timeout=10) as response:
                payload = response.read()
                self.send_response(response.status)
                self.send_header("Content-Type", response.headers.get("Content-Type", "application/json"))
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)
        except HTTPError as err:
            self._send_json({"error": err.reason}, status=err.code)
        except URLError as err:
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
    server.serve_forever()


if __name__ == "__main__":
    main()
