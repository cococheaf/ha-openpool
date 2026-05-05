# OpenPool

OpenPool is an OpenSource Pool System Controller for Home Assistant.

This add-on serves the OpenPool web UI through Home Assistant Ingress and
provides a small internal proxy for Home Assistant Core API calls.

## Installation

1. Push this repository to GitHub.
2. Replace the placeholder repository URL in `repository.yaml` and
   `openpool/config.yaml`.
3. In Home Assistant, go to **Settings -> Add-ons -> Add-on Store**.
4. Open **Repositories**, add your GitHub repository URL and reload the store.
5. Install **OpenPool** and enable **Show in sidebar**.

## Status

The current UI is still the single-file prototype with demo state. The add-on
packaging is ready for Home Assistant installation and provides the integration
surface for the real controller backend.
