#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
PID_DIR="$ROOT_DIR/pids"
LOG_DIR="$ROOT_DIR/logs"

mkdir -p "$PID_DIR" "$LOG_DIR"

stop_service() {
  local name="$1"
  local pid_file="$2"

  if [ -f "$pid_file" ]; then
    local pid
    pid=$(cat "$pid_file")
    if kill -0 "$pid" >/dev/null 2>&1; then
      echo "Stopping previous $name (pid $pid)"
      kill "$pid" || true
      sleep 1
    fi
    rm -f "$pid_file"
  fi
}

stop_service "backend" "$PID_DIR/backend.pid"
stop_service "frontend" "$PID_DIR/frontend.pid"

echo "Starting backend..."
nohup python -m infograph.svc.main --port 8000 > "$LOG_DIR/backend.log" 2>&1 &
echo $! > "$PID_DIR/backend.pid"
echo "Backend started (pid $(cat "$PID_DIR/backend.pid")). Logs: $LOG_DIR/backend.log"

FRONTEND_URL="http://localhost:3001"
API_URL="http://localhost:8000"

echo "Frontend URL: $FRONTEND_URL"
echo "API URL: $API_URL"

echo "Quick CLI:
  ./start.sh                            # start backend (and future frontend)
  ./stop.sh                             # stop services using PID files under pids/
  tail -f $LOG_DIR/backend.log          # inspect backend logs
  python -m infograph.svc.main --port 8000  # run the backend for debugging"
