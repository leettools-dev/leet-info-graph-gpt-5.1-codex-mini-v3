#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PIDS_DIR="$ROOT_DIR/pids"
LOGS_DIR="$ROOT_DIR/logs"
mkdir -p "$PIDS_DIR" "$LOGS_DIR"

# Stop previous backend if running
if [ -f "$PIDS_DIR/backend.pid" ]; then
  OLD_PID=$(cat "$PIDS_DIR/backend.pid") || true
  if [ -n "$OLD_PID" ] && kill -0 "$OLD_PID" >/dev/null 2>&1; then
    echo "Stopping old backend process $OLD_PID"
    kill "$OLD_PID" || true
    sleep 1
  fi
fi

# Start backend
echo "Starting backend..."
python -m backend.uvicorn_runner --host 0.0.0.0 --port 8000 > "$LOGS_DIR/backend.log" 2>&1 &
BACKEND_PID=$!
echo "$BACKEND_PID" > "$PIDS_DIR/backend.pid"
echo "Backend PID: $BACKEND_PID"

# Print frontend info (frontend may be started separately)
FRONTEND_URL="http://localhost:3001"

echo "Frontend available at $FRONTEND_URL"
