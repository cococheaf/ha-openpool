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
- PV release with optional battery priority.
- Battery logic can be disabled for installations without battery storage.
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
- `features.battery_logic` if battery sensors and battery priority should be
  used
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
  `energy.prefer_battery_charging` protects battery charging before heat-pump
  release. If the battery is not charging and PV surplus still remains,
  OpenPool treats it as full. When battery priority is enabled, configure either
  a battery discharge sensor or the shared battery power sensor; without that
  signal, OpenPool blocks PV heating fail-safe.
- Pump and heat pump sensors

`Heizung Ein`/manual heat and night swimming are intentional overrides. They
bypass PV/battery automation, but still require pump flow and the master enable.

Wrong entities can make OpenPool take bad decisions or send commands to the
wrong device.

## Installation

1. Install the add-on.
2. Check the add-on configuration and adapt the entities.
3. Start the add-on.
4. Enable **Show in sidebar**.

Technical details are in [DOCS.md](DOCS.md).
