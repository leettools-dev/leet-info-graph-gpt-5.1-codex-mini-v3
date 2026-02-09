#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOGS_DIR="$ROOT_DIR/logs"
PIDS_DIR="$ROOT_DIR/pids"
BACKEND_PID_FILE="$PIDS_DIR/backend.pid"
FRONTEND_PID_FILE="$PIDS_DIR/frontend.pid"
BACKEND_LOG_FILE="$LOGS_DIR/backend.log"
FRONTEND_LOG_FILE="$LOGS_DIR/frontend.log"
BACKEND_PORT=${BACKEND_PORT:-8000}
FRONTEND_PORT=${VITE_FRONTEND_PORT:-3001}
FRONTEND_HOST="0.0.0.0"
BACKEND_CMD="python -m infograph.svc.main"
FRONTEND_CMD="npm run dev -- --host $FRONTEND_HOST --port $FRONTEND_PORT"

ensure_directories() {
  mkdir -p "$LOGS_DIR" "$PIDS_DIR"
}

stop_if_running() {
  local pid_file="$1"
  local label="$2"

  if [[ -f "$pid_file" ]]; then
    local pid
    pid=$(<"$pid_file")
    if [[ -n "$pid" ]] && kill -0 "$pid" >/dev/null 2>&1; then
      echo "Stopping $label (pid=$pid)..."
      kill "$pid" >/dev/null 2>&1 || true
      sleep 0.2
      kill -0 "$pid" >/dev/null 2>&1 && kill -9 "$pid" >/dev/null 2>&1 || true
    fi
    rm -f "$pid_file"
  fi
}

stop_existing_processes() {
  stop_if_running "$BACKEND_PID_FILE" "backend service"
  stop_if_running "$FRONTEND_PID_FILE" "frontend dev server"
}

start_backend() {
  echo "Starting backend on port $BACKEND_PORT..."
  (cd "$ROOT_DIR/backend" && $BACKEND_CMD --host 0.0.0.0 --port "$BACKEND_PORT" >>"$BACKEND_LOG_FILE" 2>&1 &)
  local pid=$!
  echo "$pid" >"$BACKEND_PID_FILE"
  echo "Backend pid: $pid"
}

start_frontend() {
  echo "Starting frontend on port $FRONTEND_PORT..."
  (cd "$ROOT_DIR/frontend" && VITE_FRONTEND_PORT="$FRONTEND_PORT" VITE_API_BASE=${VITE_API_BASE:-http://localhost:$BACKEND_PORT} $FRONTEND_CMD >>"$FRONTEND_LOG_FILE" 2>&1 &)
  local pid=$!
  echo "$pid" >"$FRONTEND_PID_FILE"
  echo "Frontend pid: $pid"
}

main() {
  ensure_directories
  stop_existing_processes
  start_backend
  start_frontend
  echo "Logs: $LOGS_DIR"
  echo "Frontend available at http://localhost:$FRONTEND_PORT"
  echo "Use ./stop.sh to terminate services when you are done."
}

main
