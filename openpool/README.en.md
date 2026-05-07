# OpenPool

[Deutsche Version](README.md)

OpenPool is an OpenSource Pool System Controller for Home Assistant. The add-on
controls pump, chlorinator, heat pump and PV surplus heating through one compact
interface, especially suited for tablet dashboards such as an iPad in Home
Assistant.

OpenPool is currently designed around setups based on the Intex 26680 sand
filter and saltwater chlorinator system. Other systems may work, but they are
not the primary development target at the moment.

![OpenPool Dashboard Demo](../OpenPool_DemoImage.png)

## Why This Add-on Exists

OpenPool comes from a very practical family problem: a clean pool in the garden
was supposed to make summer easier, without packing up kids, swim bags and
everything else for every trip to the public pool. An Intex XTR frame pool soon
turned into a setup with a stronger sand filter and saltwater chlorinator. Water
quality improved, but the control options remained inflexible.

A Tasmota smart plug first made it possible to switch the Intex 26680 from Home
Assistant. It also revealed that the chlorinator starts again after a power
loss, which can be used as a simple restart pulse. After adding a heat pump, the
interaction became more complex: the heat pump needs safe water flow, while the
pump still has to be controlled deliberately for chlorine production.

OpenPool combines these parts into one shared logic. Home Assistant provides the
switches and sensors; OpenPool makes the decisions.

## What OpenPool Does

- Pump profiles for swim mode, bad weather mode, continuous operation, night
  swimming and off.
- Automatic restart pulses for the chlorinator.
- Chlorinator display derived from pump power with configurable power
  thresholds.
- Safe pump run-on after heat pump operation.
- Heat pump control with target temperature.
- Heat-pump release with start/stop thresholds and stability times.
- Calm weather recommendation from the Home Assistant daily forecast with two
  refreshes per day.
- Live synchronization between multiple open UI sessions.
- Persistent controller state in `/data/openpool_state.json`, so runtime, jobs
  and task history survive restarts.
- Optional weather control and heat pump control through add-on configuration.
- Weather control as recommendation or automation for swim mode and bad weather
  mode.

## Important Before The First Start

Please adapt the entities in the add-on configuration to your Home Assistant
installation before the first real test. The bundled entity IDs are examples
from the original setup.

Especially important:

- `pump_switch`
- `heater_climate`
- `weather`
- `pv_generation`
- `pv_export`
- `grid_import`
- Pump and heat pump sensors for power, current, voltage, signal and
  temperatures

If these entities are not correct, OpenPool cannot make reliable decisions or
may send commands to the wrong devices, or to no device at all.

The weather entity is not tied to a fixed provider. Put the Weather entity of
your preferred Home Assistant integration into `entities.weather`. OpenPool only
uses the broad daily class: bathing weather for mostly sunny or clear days, bad
weather for strong cloud cover or rain.

In the dashboard, weather control can be set to `Empfehlung` or `Automatik`.
With `Empfehlung`, OpenPool only shows the recommended pump profile. With
`Automatik`, OpenPool sets the pump mode to swim mode or bad weather mode.

## Home Assistant Logbook Attribution

By default, the add-on uses the Home Assistant `SUPERVISOR_TOKEN`. This avoids
any additional login, but the Home Assistant logbook shows service calls as
triggered by the Supervisor.

If the logbook should show actions as triggered by `OpenPool`, create a Home
Assistant user named `OpenPool`, create a long-lived access token in that user's
profile and configure the add-on like this:

```yaml
connection:
  auth_mode: openpool_user_token
  access_token: "TOKEN_OF_THE_OPENPOOL_USER"
```

OpenPool will then use that user token for Home Assistant service calls.

## Installation

1. In Home Assistant, open **Settings -> Add-ons -> Add-on Store**.
2. Open **Repositories**, add `https://github.com/cococheaf/ha-openpool` and
   reload the store.
3. Install **OpenPool**.
4. Adjust the add-on configuration, especially all entities.
5. Start the add-on and enable **Show in sidebar**.

## Status

The add-on serves the OpenPool web interface through Home Assistant Ingress. The
automation runs in the add-on server, not in the browser. This keeps multiple
open interfaces synchronized, and runtimes as well as scheduled jobs survive
frontend reloads and add-on restarts.
