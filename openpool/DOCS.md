# OpenPool Add-on Documentation

## Home Assistant API

The add-on is configured with `homeassistant_api: true`. At runtime, Home
Assistant provides `SUPERVISOR_TOKEN`, which the OpenPool server uses to proxy
selected API calls:

- `GET /api/ha/states/<entity_id>`
- `POST /api/ha/services/<domain>/<service>`

The browser UI should call the local add-on endpoints instead of storing a
long-lived access token in the frontend.

If the Supervisor token is not available in the add-on container, OpenPool can
fall back to the configured `connection.homeassistant_url` and
`connection.access_token` add-on options.

## Controller State

OpenPool keeps its runtime state in the add-on server, not in the browser. The
state is persisted in `/data/openpool_state.json` and contains the active modes,
pump runtime counters, pending jobs and command history.

The frontend listens to `GET /api/openpool/events` for live state updates, uses
`GET /api/openpool/state` as a fallback and sends user actions to
`POST /api/openpool/action`. This keeps multiple browser sessions in sync and
allows automation jobs to continue when the UI is closed.

## PV Release

OpenPool derives the current house consumption from PV production and grid
export: `pv_generation - pv_export`. The heat-pump PV release is then
calculated as `pv_generation - house_consumption - grid_import`. A derived
net-load sensor such as `sensor.nettobezug` is displayed for information only
and is not used as house consumption. When the heat pump is already running, its
current power sensor is added back to estimate the surplus that would exist
without the heat pump load.
OpenPool only enables the heat pump after the pump switch is confirmed on by
Home Assistant, so the pump load is already represented at the grid meter.
The add-on options control the PV release with a start threshold, stop
threshold and separate stability times. `pv_start_export_w` is the legacy option
name for the calculated available PV power needed to start the heat pump. The
heat pump starts only after that value has been reached continuously for
`pv_start_stable_minutes`. While the heat pump is running, OpenPool waits until
the available PV power stays below `pv_stop_export_w` for
`pv_stop_stable_minutes` before switching it off.

## Configuration

The add-on options contain the Home Assistant entity IDs, profile times, restart
pulses and control thresholds. The OpenPool UI is intentionally control-only;
permanent configuration changes are made in the Home Assistant add-on options.

## Files

- `/app/www`: bundled frontend
- `/data/options.json`: Home Assistant add-on options
- `/config`: writable add-on configuration directory
