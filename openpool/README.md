# OpenPool

OpenPool is an OpenSource Pool System Controller for Home Assistant.

This add-on serves the OpenPool web UI through Home Assistant Ingress and
provides a small internal proxy for Home Assistant Core API calls.

## Installation

1. In Home Assistant, go to **Settings -> Add-ons -> Add-on Store**.
2. Open **Repositories**, add `https://github.com/cococheaf/ha-openpool` and reload the store.
3. Install **OpenPool** and enable **Show in sidebar**.

## Status

The UI reads the configured Home Assistant entities through the add-on proxy and
sends manual pump, restart-pulse, heat pump mode and target-temperature commands
back to Home Assistant services.
