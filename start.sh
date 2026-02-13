#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
RUN_DIR="$ROOT_DIR/run"
LOG_DIR="$ROOT_DIR/logs"
mkdir -p "$RUN_DIR" "$LOG_DIR"

# Stop previous backend if running
if [ -f "$RUN_DIR/backend.pid" ]; then
  OLD_PID=$(cat "$RUN_DIR/backend.pid")
  if kill -0 "$OLD_PID" >/dev/null 2>&1; then
    echo "Stopping previous backend (pid $OLD_PID)"
    kill "$OLD_PID" || true
    sleep 1
  fi
  rm -f "$RUN_DIR/backend.pid"
fi

# Start backend
echo "Starting backend..."
nohup python -m infograph.svc.main --port 8000 > "$LOG_DIR/backend.log" 2>&1 &
echo $! > "$RUN_DIR/backend.pid"
echo "Backend started (pid $(cat $RUN_DIR/backend.pid)). Logs: $LOG_DIR/backend.log"

# Frontend (if present) - placeholder start
FRONTEND_URL="http://localhost:3001"

echo "Frontend URL: $FRONTEND_URL"

echo "Quick CLI:
  ./start.sh    # start services
  ./stop.sh     # stop services
  tail -f $LOG_DIR/backend.log  # inspect backend logs"
