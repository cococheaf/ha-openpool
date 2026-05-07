# OpenPool

[Deutsche Version](README.md)

OpenPool is an OpenSource Pool System Controller for Home Assistant. It controls
the pool pump, chlorinator, heat pump and PV surplus heating from one compact,
tablet-friendly interface, while the actual automation runs server-side inside
the Home Assistant add-on.

OpenPool is currently designed around setups based on the Intex 26680 sand
filter and saltwater chlorinator system. Other systems may work, but they are
not the primary development target at the moment.

![OpenPool Dashboard Demo](OpenPool_DemoImage.png)

## Why OpenPool Exists

The reason for this project was very down to earth: we wanted a clean pool in
the garden so we would not have to pack up the kids, towels, bags and half the
house every time we wanted to go swimming in summer. So the first step was an
Intex XTR frame pool set in the garden.

During the first season it quickly became clear that the filter pump included in
the set was not enough to keep the pool reliably clean. After the water went bad,
I upgraded one season later to the Intex 26680 sand filter and saltwater
chlorinator combo. Filtration and chlorine production improved a lot, but the
timing and control options of that unit were frustratingly limited in everyday
use.

As a pragmatic workaround I added a switchable Tasmota smart plug. That made it
possible to turn the system on and off from Home Assistant without walking out
to the pool every time. While doing that I noticed a useful behavior: after a
power loss, the chlorinator started again. So the internal timers of the unit
kept their role, while the actual chlorine production could be influenced by the
smart plug schedule.

When a heat pump was added later, this workaround became unreliable. The heat
pump needs water flow, but the pump also had to remain controllable for chlorine
production. The devices had no understanding of each other. That was the point
where the idea for OpenPool was born: if all switches, sensors and measurements
already exist in Home Assistant, then Home Assistant should also be able to run
the coordinated pool control logic.

I am not a strong coder myself, so OpenPool was built with the help of AI. The
result is a specialized add-on for exactly this everyday use case: keep the pool
clean, protect the heat pump, use PV surplus power and reduce the amount of
manual intervention.

## Project Goal

OpenPool is meant to automate pool operation reliably without taking control
away from the user. The interface intentionally stays simple: it shows the
current state, upcoming tasks, important sensor values and the central operating
modes. Permanent configuration lives in the Home Assistant add-on options.

The goal is not to be a universal pool control system for every imaginable
installation. OpenPool is built for real Home Assistant use: enter the existing
entities, enable the control logic, open the dashboard and see what is happening.

## What OpenPool Can Do

- Control pump modes: Off, continuous operation, swim mode, bad weather mode and
  night swimming.
- Run automatic pump profiles with configurable start and end times.
- Execute restart pulses for the chlorinator, using short power-off pulses to
  restart chlorine production.
- Derive the chlorinator status from pump power, using configurable pump power
  values without and with the chlorinator.
- Release the heat pump only after confirmed pump flow.
- Keep the pump running after heat pump operation for a safe run-on period.
- Calculate PV surplus for the heat pump and start heating only after a stable
  heat-pump release condition.
- Configure heat-pump start and stop thresholds as well as stability times.
- Evaluate the daily forecast of the configured Home Assistant weather entity
  and recommend swim mode or bad weather mode.
- Set the heat pump target temperature from the UI.
- Store runtimes, upcoming tasks and command history server-side.
- Keep multiple open interfaces synchronized, for example iPad, smartphone and
  a desktop browser.
- Persist controller state in `/data/openpool_state.json`, so runtimes and jobs
  survive add-on restarts.

## How The System Works

OpenPool runs as a Home Assistant add-on. The web UI is served through Home
Assistant Ingress, while the Python controller inside the add-on owns the actual
runtime state and executes actions. Browser, iPad and smartphone sessions do not
talk directly to Home Assistant; they talk to the OpenPool server. This keeps
all open sessions on the same state.

The controller regularly reads the configured Home Assistant entities,
calculates the OpenPool state from them and sends service calls back to Home
Assistant when needed. The update rate can be configured with `poll_interval_s`.

For heat-pump release, house consumption is derived from PV production, balancing grid
export and grid import:

```text
house consumption = PV production - grid export + grid import
available for heat pump = PV production - house consumption
```

When the heat pump is already running, its current power is added back. This
prevents the heat pump from immediately switching itself off just because its
own load reduces the visible surplus.

## Important Before The First Start

The entities in the add-on configuration must be adapted to your Home Assistant
installation before the first real test. The default values are examples from
the original installation and will probably not match your system unchanged.

Check especially:

- `pump_switch`: switch for pump or pump/chlorinator system.
- `heater_climate`: climate entity of the heat pump.
- `weather`: weather entity.
- `pv_generation`: current PV production.
- `pv_export`: balancing grid export from the smart meter.
- `grid_import`: grid import from the smart meter.
- Pump and heat pump sensors for power, current, voltage, signal and
  temperatures.

If these entities are wrong, OpenPool may start, but it cannot make reliable
decisions or send commands to the correct devices.

## Home Assistant Logbook Attribution

By default, OpenPool uses the `SUPERVISOR_TOKEN` provided by Home Assistant.
This works without any additional token, but Home Assistant will attribute
service calls in the logbook to the Supervisor.

If the Home Assistant logbook should show actions as triggered by `OpenPool`,
create a dedicated Home Assistant user named `OpenPool`, create a long-lived
access token in that user's profile and configure the add-on like this:

```yaml
connection:
  auth_mode: openpool_user_token
  access_token: "TOKEN_OF_THE_OPENPOOL_USER"
```

Only this mode can cleanly attribute logbook entries to `OpenPool`, because Home
Assistant attributes API calls to the authenticated user behind the token.

## Installation As Home Assistant Add-on

1. In Home Assistant, open **Settings -> Add-ons -> Add-on Store**.
2. Open **Repositories** and add:
   `https://github.com/cococheaf/ha-openpool`
3. Reload the store, install **OpenPool** and enable **Show in sidebar**.
4. Before starting, check the add-on configuration and adapt all entities.
5. Start the add-on and open the web interface from the Home Assistant sidebar.

## Project Status

- `openpool/` contains the Home Assistant add-on and bundled UI.
- The add-on serves the UI through Home Assistant Ingress.
- The OpenPool controller owns the shared state and executes pump, restart-pulse
  and heat pump automation.
- Open UI sessions receive the shared controller state live from the add-on, so
  browser, tablet and smartphone stay synchronized.

## Development

For the add-on build, Home Assistant uses `openpool/config.yaml` and
`openpool/Dockerfile`. The bundled frontend lives in `openpool/www/index.html`.
