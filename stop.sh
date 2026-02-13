#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
RUN_DIR="$ROOT_DIR/run"
LOG_DIR="$ROOT_DIR/logs"

if [ -f "$RUN_DIR/backend.pid" ]; then
  PID=$(cat "$RUN_DIR/backend.pid")
  if kill -0 "$PID" >/dev/null 2>&1; then
    echo "Stopping backend (pid $PID)"
    kill "$PID" || true
    sleep 1
  fi
  rm -f "$RUN_DIR/backend.pid"
  echo "Backend stopped"
else
  echo "No backend pid file found"
fi

if [ -f "$RUN_DIR/frontend.pid" ]; then
  PID=$(cat "$RUN_DIR/frontend.pid")
  if kill -0 "$PID" >/dev/null 2>&1; then
    echo "Stopping frontend (pid $PID)"
    kill "$PID" || true
    sleep 1
  fi
  rm -f "$RUN_DIR/frontend.pid"
  echo "Frontend stopped"
else
  echo "No frontend pid file found"
fi
