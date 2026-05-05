# OpenPool

OpenPool is an OpenSource Pool System Controller for Home Assistant. It is
intended to control an Intex pump/chlorinator system, a pool heat pump and PV
surplus based heating logic from one compact tablet-friendly interface.

## Current State

- `openpool/` contains the Home Assistant add-on and bundled UI.
- The add-on serves the UI through Home Assistant Ingress and includes a small
  API proxy for Home Assistant state reads and service calls.

## Install As Home Assistant Add-on

1. Push this folder to your GitHub repository.
2. In Home Assistant open **Settings -> Add-ons -> Add-on Store**.
3. Open **Repositories** and add `https://github.com/cococheaf/ha-openpool`.
4. Reload the store, install **OpenPool**, then enable **Show in sidebar**.

## Development

For the add-on build, Home Assistant uses `openpool/config.yaml` and
`openpool/Dockerfile`. The bundled frontend lives in `openpool/www/index.html`.

The add-on is modeled after the repository-based installation flow used by
projects such as evcc, where Home Assistant users add a GitHub add-on
repository to the Add-on Store.
