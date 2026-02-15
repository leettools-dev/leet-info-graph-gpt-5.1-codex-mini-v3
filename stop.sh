#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
PID_DIR="$ROOT_DIR/pids"
LOG_DIR="$ROOT_DIR/logs"

stop_service() {
  local name="$1"
  local pid_file="$2"

  if [ -f "$pid_file" ]; then
    local pid
    pid=$(cat "$pid_file")
    if kill -0 "$pid" >/dev/null 2>&1; then
      echo "Stopping $name (pid $pid)"
      kill "$pid" || true
      sleep 1
    fi
    rm -f "$pid_file"
  fi
}

stop_service "backend" "$PID_DIR/backend.pid"
stop_service "frontend" "$PID_DIR/frontend.pid"

echo "Services stopped."
