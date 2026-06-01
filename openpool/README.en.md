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
  Assistant selector, run-on protection and optional PV automation.
- Weather control as recommendation or automation.
- Live sync between multiple browsers and persistent state in
  `/data/openpool_state.json`.

## Before First Start

Adapt all entities in the add-on configuration to your Home Assistant setup.
Most important:

- `entities.control.pump_switch`
- `entities.control.heater_climate`
- `entities.control.heater_operation_mode`
- `entities.control.weather`
- `entities.energy.pv_generation`
- Energy/grid: either `entities.energy.pv_export` and
  `entities.energy.grid_import` or `entities.energy.grid_power` with
  `entities.energy.use_combined_grid_sensor` and the matching sign option
  `entities.energy.grid_power_import_positive`
- Pump and heat pump sensors

Wrong entities can make OpenPool take bad decisions or send commands to the
wrong device.

## Installation

1. Install the add-on.
2. Check the add-on configuration and adapt the entities.
3. Start the add-on.
4. Enable **Show in sidebar**.

Technical details are in [DOCS.md](DOCS.md).
