#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PIDS_DIR="$ROOT_DIR/pids"

if [ -f "$PIDS_DIR/backend.pid" ]; then
  PID=$(cat "$PIDS_DIR/backend.pid") || true
  if [ -n "$PID" ] && kill -0 "$PID" >/dev/null 2>&1; then
    echo "Stopping backend $PID"
    kill "$PID" || true
    rm -f "$PIDS_DIR/backend.pid"
  else
    echo "No running backend found"
    rm -f "$PIDS_DIR/backend.pid" || true
  fi
else
  echo "No PID file for backend"
fi
