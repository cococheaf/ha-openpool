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

The add-on options contain the default Home Assistant entity IDs and control
thresholds. The same values are visible inside the OpenPool UI under
**Konfiguration**; saving there stores a browser-local override for the current
Home Assistant frontend session.

## Files

- `/app/www`: bundled frontend
- `/data/options.json`: Home Assistant add-on options
- `/config`: writable add-on configuration directory
