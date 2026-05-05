# Changelog

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
