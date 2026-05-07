# OpenPool

[Deutsche Version](README.md)

OpenPool is an open source pool system controller for Home Assistant. The add-on
controls the pump, chlorinator, heat pump, weather profiles and PV surplus
heating from one compact web interface. The actual automation runs server-side
inside the Home Assistant add-on, so browser, iPad and smartphone sessions all
see the same state.

OpenPool is currently designed for setups based on the Intex 26680 sand filter
and saltwater chlorinator system. Other systems may work, but they are not the
primary development target yet.

## Screenshots

| Desktop | Tablet | iPhone |
| --- | --- | --- |
| ![OpenPool Desktop](docs/screenshots/openpool-desktop.png) | ![OpenPool Tablet](docs/screenshots/openpool-tablet.png) | ![OpenPool iPhone](docs/screenshots/openpool-iphone.png) |

## Why OpenPool Exists

OpenPool started with an Intex frame pool that should stay clean through summer
without constant manual work. The original filter pump was too weak, and the
later Intex 26680 sand filter and saltwater chlorinator combo was much better
but still limited in its timing options. A Tasmota smart plug made switching
more convenient and also showed that the chlorinator restarts after a short
power loss.

After adding a heat pump, this became a real control problem: the heat pump
needs safe water flow, while the pump still has to be controlled for chlorine
production and operating profiles. OpenPool connects this logic to the Home
Assistant entities that already exist in the installation.

## Features

- Pump profiles: off, continuous operation, swim mode, bad weather mode and
  night swimming.
- Configurable night swimming duration and restart pulses for the chlorinator.
- Chlorinator detection from pump power.
- Heat pump control with target temperature, pump run-on and optional PV
  automation.
- PV release with start/stop thresholds and stability times.
- Weather control as recommendation or automation for swim mode and bad weather
  mode.
- Provider-neutral weather entity with only two forecast refreshes per day.
- Live sync between multiple open interfaces.
- Persistent controller state in `/data/openpool_state.json`.
- Configuration through Home Assistant add-on options.

## Important Before First Start

The entity IDs in the add-on configuration must be adapted to your Home
Assistant installation before the first live test. The defaults are only
examples from the original OpenPool setup.

Especially important:

- `entities.pump_switch`
- `entities.heater_climate`
- `entities.weather`
- `entities.pv_generation`
- `entities.pv_export`
- `entities.grid_import`
- Pump and heat pump sensors for power, current, voltage, signal and
  temperatures

If these entities do not match your system, OpenPool may start but cannot make
reliable decisions or send commands to the correct devices.

## Installation

1. In Home Assistant, open **Settings -> Add-ons -> Add-on Store**.
2. Under **Repositories**, add:
   `https://github.com/cococheaf/ha-openpool`
3. Reload the store and install **OpenPool**.
4. Adjust the add-on configuration, especially all entities.
5. Start the add-on and enable **Show in sidebar**.

## Documentation

- Add-on documentation: [openpool/DOCS.md](openpool/DOCS.md)
- Changelog: [openpool/CHANGELOG.md](openpool/CHANGELOG.md)
- Home Assistant add-on: [openpool/](openpool/)

## Releases

Versioned releases are created from Git tags in the `vX.Y.Z` format. When a tag
is pushed, GitHub Actions automatically creates a GitHub release from the
matching section in `openpool/CHANGELOG.md`.
