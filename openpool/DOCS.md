# OpenPool Add-on Documentation

## Home Assistant API

The add-on is configured with `homeassistant_api: true`. At runtime, Home
Assistant provides `SUPERVISOR_TOKEN`, which the OpenPool server uses to proxy
selected API calls:

- `GET /api/ha/states/<entity_id>`
- `POST /api/ha/services/<domain>/<service>`

The browser UI should call the local add-on endpoints instead of storing a
long-lived access token in the frontend.

## Configuration

Most OpenPool settings are currently visible inside the OpenPool UI under
**Konfiguration**. The add-on configuration only contains operational settings
needed before the web app starts.

## Files

- `/app/www`: bundled frontend
- `/data/options.json`: Home Assistant add-on options
- `/config`: writable add-on configuration directory
