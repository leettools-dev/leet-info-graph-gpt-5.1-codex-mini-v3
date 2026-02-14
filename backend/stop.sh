#!/usr/bin/env bash
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_FILE="$BASE_DIR/backend.pid"

if [ -f "$PID_FILE" ]; then
  PID=$(cat "$PID_FILE")
  echo "Stopping backend process $PID"
  kill "$PID"
  rm -f "$PID_FILE"
  echo "Stopped"
else
  echo "No PID file found"
fi
