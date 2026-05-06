# Changelog

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
