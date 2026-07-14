# OpenPool Add-on Documentation

![OpenPool Desktop Dashboard](../docs/screenshots/openpool-desktop.png)

## Home Assistant API

The add-on is configured with `homeassistant_api: true`. At runtime, Home
Assistant provides `SUPERVISOR_TOKEN`, which the OpenPool server uses to proxy
selected API calls:

- `GET /api/ha/states/<entity_id>`
- `POST /api/ha/services/<domain>/<service>`

The browser UI should call the local add-on endpoints instead of storing a
long-lived access token in the frontend.

Daily weather forecasts are read server-side with
`weather.get_forecasts?return_response` for the configured
`devices.weather_service` entity. The forecast is cached for 12 hours and
persisted in the OpenPool state file. Normal one-second sensor polling does not
read the weather entity.

If the Supervisor token is not available in the add-on container, OpenPool can
fall back to the configured `connection.homeassistant_url` and
`connection.access_token` add-on options.

`connection.auth_mode` controls which token source is preferred:

- `supervisor`: use `SUPERVISOR_TOKEN` first and only fall back to
  `connection.access_token` if the Supervisor token is unavailable.
- `openpool_user_token`: always use `connection.access_token`. Use this with a
  dedicated Home Assistant user named `OpenPool` when logbook entries should be
  attributed to OpenPool instead of Supervisor.

## Controller State

OpenPool keeps its runtime state in the add-on server, not in the browser. The
state is persisted in `/data/openpool_state.json` and contains the active modes,
pump runtime counters, pending jobs and command history.

The frontend listens to `GET /api/openpool/events` for live state updates, uses
`GET /api/openpool/state` as a fallback and sends user actions to
`POST /api/openpool/action`. This keeps multiple browser sessions in sync and
allows automation jobs to continue when the UI is closed.

## Backups

OpenPool uses `backup: cold` in its add-on metadata. Home Assistant Supervisor
therefore stops OpenPool briefly while creating an add-on backup, then starts it
again afterwards. This avoids hot-backup races with `/data/openpool_state.json`,
which is updated frequently while the controller is running. Transient
`*.tmp` files from atomic state writes are excluded from backups.

## Heat Pump Run-on

Any planned pump stop is protected by the heat pump run-on rule. Before a pump
profile ends and before Nachtbaden reaches its maximum duration, OpenPool
switches the heat pump off five minutes early and keeps the pump running for
flow. If a manual pump-off action happens while the heat pump is running or has
stopped less than five minutes ago, the pump remains on until the remaining
run-on time has completed. Restart pulses are intentionally exempt from this
rule because they only stop the pump for a few seconds.

## Heat Pump Release

OpenPool calculates heat-pump release from the current grid balance and optional
battery power. With separate grid sensors, `energy.grid_export_sensor` is treated
as export/feed-in and `energy.grid_import_sensor` as import. If
`energy.one_grid_sensor_for_import_and_export` is enabled, OpenPool reads
`energy.shared_grid_power_sensor` instead. With
`energy.positive_grid_value_is_import` enabled, positive values are grid import
and negative values are export/feed-in; disabling the option reverses that sign
direction.

Battery storage can be configured with one signed sensor or two separate
sensors. For one signed value, enable
`energy.one_battery_sensor_for_charge_and_discharge`, set
`energy.shared_battery_power_sensor` and choose the sign direction with
`energy.positive_battery_value_is_charge`. For separate values, set
`energy.battery_charge_sensor` and/or `energy.battery_discharge_sensor`.
Unconfigured battery sensors count as `0 W`.

The available heat-pump power starts as `grid_export - grid_import`. Battery
discharge is always subtracted because the heat pump should not start from
battery energy. If `energy.prefer_battery_charging` is disabled, current battery
charging is added back and may be redirected to the heat pump. If it is enabled,
OpenPool protects battery charging and releases the heat pump only from surplus
that remains after house load and battery charging. When the heat pump is
already running, its current power sensor is normally added back to estimate the
surplus that would exist without the heat pump load. With battery priority
enabled, that add-back is suppressed as soon as battery discharge is detected,
and OpenPool turns the heat pump off immediately above a small discharge
tolerance instead of waiting for the normal PV stop stability time.
OpenPool only enables the heat pump after the pump switch is confirmed on by
Home Assistant, so the pump load is already represented at the grid meter.
The add-on options control the heat-pump release with a start threshold, stop
threshold and separate stability times. The heat pump starts only after enough
PV power has been available continuously for the configured start stability
time. While the heat pump is running, OpenPool waits until the available PV
power stays below the stop threshold for the configured stop stability time
before switching it off.

## Heat Pump Start Mode

If `devices.heat_pump_operating_mode` points to a Home Assistant `select`
entity, OpenPool reads the available start modes directly from that entity's
`attributes.options`. The UI dropdown therefore follows the actual modes
provided by the heat pump integration. The selected value is persisted in
`/data/openpool_state.json` and is preserved during add-on restarts even before
Home Assistant has reported the available choices again. If the heat pump is
already running after an add-on restart, OpenPool re-applies the stored mode
when the control loop resumes.

## Pump Profiles

Profile times are configured in the add-on `profiles` section. Nachtbaden uses
`profiles.night_swim_duration_hours` as its maximum runtime. The dashboard
labels, the upcoming task and the automatic Nachtbaden shutdown all use this
same add-on option.

Restart pulses use one shared duration from
`restart_pulses.pulse_duration_s` (`Pulse-Dauer`). This value defines how many
seconds the pump stays off between pulse start and pulse stop. It is used for
manual, scheduled and 12-hour restart pulses.

## Weather Recommendation

OpenPool uses the configured Home Assistant weather entity, for example
`weather.home`, `weather.openweathermap` or another provider-specific weather
entity, and asks Home Assistant for the daily forecast at most twice per day.
The recommendation is intentionally coarse:

- `Badewetter`: `sunny`, `clear-night` or `partlycloudy`.
- `Schlechtwetter`: strongly cloudy, rain, storms, fog, snow or exceptional
  weather states.

The dashboard shows the resulting daily class and the recommended pump profile.
The weather card has a persistent `Empfehlung`/`Automatik` switch:

- `Empfehlung`: OpenPool only displays the recommended pump profile.
- `Automatik`: OpenPool sets the pump profile to `Badebetrieb` or
  `Schlechtwetter` according to the cached daily recommendation.

Manual pump-mode changes pause weather automation and switch it back to
`Empfehlung`. Heat-pump control is intentionally independent from weather and is
handled by manual heat mode or PV automation.

## Feature Switches

`features.heat_pump_control` disables heat-pump polling, heat-pump service
calls, heat-pump UI cards, heat-pump run-on handling and PV heating logic when
set to `false`.

`features.weather_control` disables weather forecast polling, the weather
forecast card and the weather-dependent pump automation switch when set to
`false`.
The weather provider itself is selected only through `devices.weather_service`.

## Configuration

The add-on options contain the Home Assistant entity IDs, profile times, restart
pulses and control thresholds. The OpenPool UI is intentionally control-only;
permanent configuration changes are made in the Home Assistant add-on options.
Before the first live run, all entity IDs in the add-on configuration must be
adapted to the local Home Assistant installation. The defaults are examples from
the original OpenPool setup; wrong entities can prevent control actions or send
them to the wrong device.

The dashboard derives the chlorinator status from the configured pump power
sensor. `pump_power_without_chlorinator_w` is the expected pump-only reference
load, while `pump_power_with_chlorinator_w` is the threshold from which the
chlorinator tile shows `EIN`.

## Files

- `/app/www`: bundled frontend
- `/data/options.json`: Home Assistant add-on options
- `/config`: writable add-on configuration directory
