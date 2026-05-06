# Changelog

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
