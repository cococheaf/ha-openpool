# OpenPool

[Deutsche Version](README.md)

OpenPool is a Home Assistant add-on for compact pool control around the pump,
chlorinator, heat pump, weather profile and PV surplus. It is currently designed
for setups based on the Intex 26680 sand filter and saltwater chlorinator
system.

## Features

- Pump profiles: off, continuous operation, swim mode, bad weather and night
  swimming.
- Restart pulses for the chlorinator with configurable pulse duration.
- Heat-pump control with target temperature, start operating mode from a Home
  Assistant selection list, run-on protection and optional PV automation.
- Weather control as recommendation or automation.
- Live sync between multiple browsers and persistent state in
  `/data/openpool_state.json`.

## Before First Start

Adapt all entities in the add-on configuration to your Home Assistant setup.
Most important:

- `devices.pump_and_chlorinator_switch`
- `devices.heat_pump`
- `devices.heat_pump_operating_mode`
- `devices.weather_service`
- `energy.pv_production_sensor`
- Energy/grid: either `energy.grid_export_sensor` and
  `energy.grid_import_sensor` or `energy.shared_grid_power_sensor` with
  `energy.one_grid_sensor_for_import_and_export` and the matching sign option
  `energy.positive_grid_value_is_import`
- Pump and heat pump sensors

Wrong entities can make OpenPool take bad decisions or send commands to the
wrong device.

## Installation

1. Install the add-on.
2. Check the add-on configuration and adapt the entities.
3. Start the add-on.
4. Enable **Show in sidebar**.

Technical details are in [DOCS.md](DOCS.md).
