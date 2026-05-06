# OpenPool

OpenPool is an OpenSource Pool System Controller for Home Assistant.

This add-on serves the OpenPool web UI through Home Assistant Ingress and runs
the OpenPool controller for pump profiles, restart pulses, pump run-on and PV
based heat pump decisions.

## Installation

1. In Home Assistant, go to **Settings -> Add-ons -> Add-on Store**.
2. Open **Repositories**, add `https://github.com/cococheaf/ha-openpool` and reload the store.
3. Install **OpenPool** and enable **Show in sidebar**.

## Status

The add-on keeps shared controller state in `/data/openpool_state.json` and
streams it to every open UI session, so multiple browsers stay in sync and
runtime counters survive add-on restarts.
