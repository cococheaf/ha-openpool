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
- Heat pump control with target temperature, start operating mode from a Home
  Assistant selector, pump run-on and optional PV automation.
- PV release with start/stop thresholds, stability times and optional battery
  priority.
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

- `devices.pump_and_chlorinator_switch`
- `devices.heat_pump`
- `devices.heat_pump_operating_mode`
- `devices.weather_service`
- `energy.pv_production_sensor`
- Energy/grid/battery: either `energy.grid_export_sensor` and
  `energy.grid_import_sensor` or `energy.shared_grid_power_sensor` with
  `energy.one_grid_sensor_for_import_and_export` and the matching sign option
  `energy.positive_grid_value_is_import`. For battery storage, use either
  `energy.shared_battery_power_sensor` with
  `energy.one_battery_sensor_for_charge_and_discharge` and
  `energy.positive_battery_value_is_charge`, or the separate
  `energy.battery_charge_sensor` and `energy.battery_discharge_sensor`.
  `energy.battery_soc_sensor` optionally displays the battery state of charge.
  `energy.battery_discharge_threshold_w` sets which short battery-discharge
  spike is still tolerated while battery priority is enabled.
  `energy.prefer_battery_charging` makes OpenPool release the heat pump only
  when enough PV surplus remains after house consumption and battery charging.
- Pump and heat pump sensors for power, current, voltage, signal and
  temperatures

If these entities do not match your system, OpenPool may start but cannot make
reliable decisions or send commands to the correct devices.

## Installation

1. In Home Assistant, open **Settings -> Add-ons -> Add-on Store**.
2. Under **Repositories**, add this repository:
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
