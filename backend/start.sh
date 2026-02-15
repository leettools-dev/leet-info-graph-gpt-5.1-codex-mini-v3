#!/usr/bin/env bash
# Start script for Infograph backend
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_FILE="$BASE_DIR/backend.pid"
LOG_FILE="$BASE_DIR/backend.log"

# Ensure backend package can be imported when running as a module
export PYTHONPATH="$BASE_DIR/src:$PYTHONPATH"

# Stop old process if exists
if [ -f "$PID_FILE" ]; then
  OLD_PID=$(cat "$PID_FILE")
  if kill -0 "$OLD_PID" > /dev/null 2>&1; then
    echo "Stopping old backend process $OLD_PID"
    kill "$OLD_PID"
    sleep 1
  fi
  rm -f "$PID_FILE"
fi

# Activate venv if exists
if [ -f "$BASE_DIR/.venv/bin/activate" ]; then
  source "$BASE_DIR/.venv/bin/activate"
fi

# Start server
echo "Starting backend..."
nohup python -m infograph.svc.main --port 8000 > "$LOG_FILE" 2>&1 &
NEW_PID=$!
echo "$NEW_PID" > "$PID_FILE"

echo "Backend started with PID $NEW_PID"
echo "Logs: $LOG_FILE"

echo "Visit http://localhost:8000/api/docs to view API docs"