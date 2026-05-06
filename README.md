# OpenPool

OpenPool is an OpenSource Pool System Controller for Home Assistant. It is
intended to control an Intex pump/chlorinator system, a pool heat pump and PV
surplus based heating logic from one compact tablet-friendly interface.

## Current State

- `openpool/` contains the Home Assistant add-on and bundled UI.
- The add-on serves the UI through Home Assistant Ingress, owns the OpenPool
  controller state and executes pump, restart-pulse and heating automation.

## Install As Home Assistant Add-on

1. Push this folder to your GitHub repository.
2. In Home Assistant open **Settings -> Add-ons -> Add-on Store**.
3. Open **Repositories** and add `https://github.com/cococheaf/ha-openpool`.
4. Reload the store, install **OpenPool**, then enable **Show in sidebar**.

## Development

For the add-on build, Home Assistant uses `openpool/config.yaml` and
`openpool/Dockerfile`. The bundled frontend lives in `openpool/www/index.html`.
