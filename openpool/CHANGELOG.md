# Changelog

## 0.2.30

- Rework the dashboard control panel into uniform fixed-size buttons.
- Rename Wetterprognose to Wettersteuerung and show Deaktiviert/Aktiviert for
  weather automation while keeping the existing control behavior.
- Remove visible weather forecast tiles and move the current weather
  recommendation into the weather automation tooltip.
- Split Aufgabenverlauf and Sensoren into two equal-width desktop columns.

## 0.2.29

- Rebuild the dashboard order as Allgemein, Steuerelemente, Aufgabenverlauf and
  Sensorik.
- Combine Wetterprognose, Pumpenmodus and Heizungsmodus into one large control
  card with horizontal separators.
- Color EIN/AUS status values in the main status tiles and center tile content
  across the dashboard.
- Remove the dashboard heat-pump release card and simplify tomorrow/overmorrow
  weather tiles.

## 0.2.28

- Hide explanatory dashboard tile text and expose it as hover/focus tooltips.
- Reduce the shared tile height for a cleaner, more compact dashboard layout.
- Keep dynamic hints such as Nachtbaden duration, runtime, chlorinator state and
  heat-pump source details synchronized with their tile tooltip.

## 0.2.27

- Use the configured `profiles.night_swim_max_minutes` value in all dashboard
  Nachtbaden labels and command text.
- Align status, pump mode, weather mode, weather recommendation, temperature
  and heat-pump release tiles to one shared dashboard tile size.
- Compact the weather recommendation tiles so they match the rest of the
  control surface.

## 0.2.26

- Normalize dashboard tile sizing across weather, pump, heat-pump, status and
  energy-flow cards.
- Stop pump and heat-pump mode buttons from stretching to fill the full card
  height.
- Keep the heat-pump release energy-flow tiles compact while preserving the
  centered arrow layout on small screens.

## 0.2.25

- Respect the configured add-on `log_level` for OpenPool server logs.
- Move normal Home Assistant `GET` state polling and HTTP access logs to
  `debug`.
- Keep Home Assistant service calls and OpenPool startup information visible at
  `info`.
- Keep Home Assistant API failures and controller errors visible at
  `warning`/`error`.

## 0.2.24

- Move weather automation from heat-pump control to pump-profile control.
- Add a persistent dashboard switch for weather `Empfehlung` versus
  `Automatik`.
- In weather automation, switch only between `Badebetrieb` and
  `Schlechtwetter`.
- Pause weather automation when the pump mode is selected manually.
- Remove the heat-pump `Wetterautomatik` mode and migrate old states to
  `PV-Automatik`.

## 0.2.23

- Fetch Home Assistant daily weather forecasts at most twice per day and persist
  the cached forecast across add-on restarts.
- Remove weather from the one-second live entity polling loop.
- Simplify weather evaluation to `Badewetter` versus `Schlechtwetter`.
- In weather automation, allow PV heat-pump control only when the cached daily
  recommendation is `Badewetter`.
- Remove obsolete weather rain/temperature threshold options.

## 0.2.22

- Add add-on feature switches for heat pump control and weather control.
- Skip heat-pump entities, UI cards and control actions when heat pump control
  is disabled.
- Make the default weather entity provider-neutral and keep provider selection
  in the add-on entity options.
- Add a GitHub Actions release workflow for tagged OpenPool releases.

## 0.2.21

- Fetch daily Home Assistant weather forecasts through `weather.get_forecasts`
  and base the weather recommendation on condition, rain probability,
  precipitation and minimum bathing temperature settings.
- Add date-aware task history and Upcoming labels with Heute, Gestern, Morgen
  or short dates.
- Tighten the dashboard grid and card spacing for a more compact iPad view.

## 0.2.20

- Add configurable pump power thresholds for chlorinator detection.
- Derive the dashboard chlorinator tile from the pump power sensor, showing EIN
  from the configured chlorinator threshold and AUS below it.

## 0.2.19

- Derive the dashboard heat energy source from live power values instead of the
  selected operating mode, showing KEINE, PV, PV/NETZ or NETZ.

## 0.2.18

- Only show and log the planned heat-pump pre-stop task when Home Assistant
  currently reports the heat pump as active.

## 0.2.17

- Clear stale PV stability timers after heat-pump start/stop actions.
- Hide the heat-pump start Upcoming task when the PV release is no longer
  currently valid or its countdown has already expired.

## 0.2.16

- Replace the dashboard surplus metric with a heat energy source tile that
  shows PV for automatic surplus heating and NETZ for manual heating modes.

## 0.2.15

- Add `connection.auth_mode` so installations can keep the Supervisor token or
  deliberately use a dedicated OpenPool Home Assistant user token for logbook
  attribution.

## 0.2.14

- Make the task history scrollable and keep up to 15 entries.
- Add pump and heat-pump Home Assistant switch actions to the task history.

## 0.2.13

- Rename the surplus stability Upcoming task to `Wärmepumpe startet`.
- Use clearer heat-pump release wording across the dashboard and documentation.

## 0.2.12

- Show the heat-pump start countdown as an Upcoming task while PV or weather heating automation is waiting for stable surplus.

## 0.2.11

- Correct house consumption calculation to include grid import.
- Remove the net-load display from the dashboard energy values.
- Stop using the legacy net-load sensor in OpenPool entity polling.

## 0.2.10

- Restore immediate restart pulses without switching the heat pump off first.
- Keep the heat-pump run-on protection for profile endings, Nachtbaden expiry and manual pump-off actions.

## 0.2.9

- Switch the heat pump off five minutes before planned pump stops from profile endings or restart pulses.
- Keep the pump running for the remaining heat-pump run-on time when a profile ends or the pump is manually switched off.
- Delay manual and automatic restart pulses until the heat pump run-on time has completed.

## 0.2.8

- Add configurable PV start/stop thresholds and stability times for heat-pump release.
- Keep PV release stability state in the shared controller state so browser sessions show the same control basis.
- Show the configured PV start stability time in the dashboard PV release tile.

## 0.2.7

- Rename the command card to `Aufgabenverlauf`.
- Show the next known OpenPool task as an `Upcoming:` line above the task history.

## 0.2.6

- Add configurable `poll_interval_s`, defaulting to one-second Home Assistant polling and UI live updates.
- Add a PV production sensor and derive house consumption as PV production minus grid export.
- Base PV heat-pump release on PV production, calculated house consumption and grid import.

## 0.2.5

- Only allow heat-pump control after the pump switch is confirmed on by Home Assistant, so pump load and flow are accounted for before PV heating starts.

## 0.2.4

- Calculate PV heat-pump availability from grid export minus grid import instead of subtracting a net-load sensor again.
- Keep `sensor.nettobezug` as an informational energy value and use it as the default net-load sensor.
- Add current heat-pump power back into PV availability while the heat pump is running, avoiding self-canceling PV release decisions.

## 0.2.3

- Enforce the configured maximum duration for Nachtbaden and shut down with the heater pump run-on sequence.
- Run scheduled restart pulses only inside the configured time window and only while the active pump profile should run.
- After a restart pulse, reapply the active pump profile instead of blindly switching the pump on.

## 0.2.2

- Remove the web UI settings page and navigation; configuration now lives only in the Home Assistant add-on options.
- Rework the dashboard grid and header responsiveness for desktop, iPad/tablet and phone widths.

## 0.2.1

- Add server-sent live state updates so multiple browser sessions stay in sync.
- Disable browser caching for UI, API and Home Assistant proxy responses.
- Add a polling fallback for browsers or ingress sessions where the live stream is interrupted.

## 0.2.0

- Move OpenPool control state and automation jobs into the add-on server.
- Persist controller state, pump runtimes, pending jobs and command history under `/data`.
- Add shared `/api/openpool/state` and `/api/openpool/action` endpoints for all browsers.
- Start the add-on through `with-contenv` so `SUPERVISOR_TOKEN` is available without a long-lived token.
- Add automatic pump profiles, restart pulses, pump run-on and PV heating decisions in the server controller.

## 0.1.5

- Remove Home Assistant entity and API forms from the web settings view.
- Show categorized live sensor values on the dashboard and remove the Info tab.
- Log proxied Home Assistant service calls and disable caching for the HTML shell.

## 0.1.4

- Add a Home Assistant URL and long-lived access token fallback when the Supervisor token is unavailable.
- Hide configured fallback tokens from the frontend configuration response.
- Log the selected Home Assistant authentication mode at startup.

## 0.1.3

- Fix Home Assistant Ingress API paths so frontend requests reach the add-on proxy.

## 0.1.2

- Connect UI cards and controls to the Home Assistant API proxy.
- Add add-on options for Home Assistant entities and control thresholds.
- Send pump, restart-pulse, heat pump mode and target-temperature actions to Home Assistant services.

## 0.1.1

- Remove Bashio dependency from startup script.

## 0.1.0

- Initial Home Assistant add-on packaging.
- Static OpenPool UI served through Ingress.
- Minimal Home Assistant API proxy for future backend integration.
