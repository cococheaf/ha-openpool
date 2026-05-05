#!/usr/bin/env bash
set -euo pipefail

CONFIG_PATH=/data/options.json
LOG_LEVEL="info"

if [[ -f "${CONFIG_PATH}" ]]; then
  LOG_LEVEL="$(bashio::config 'log_level' || echo info)"
fi

bashio::log.info "Starting OpenPool web app on port 8099"
export OPENPOOL_LOG_LEVEL="${LOG_LEVEL}"
exec python3 /app/server.py
