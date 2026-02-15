# Research Infograph Assistant

> Autonomous prototype that lets researchers sign in with Google, submit prompts, and receive AI-powered infographics supported by FastAPI, Vue 3, DuckDB, and TailwindCSS.

## Overview

This project is focused on building the backend and frontend skeletons for a consumer-facing research assistant. The current milestone covers the FastAPI backend service, its Click CLI entrypoint, health endpoint, and the supporting tooling (start/stop scripts, Docker workflow, and automated tests) needed to validate the foundation.

## Features

- Minimal FastAPI backend registered under `infograph.svc`, including a Click CLI in `infograph.svc.main` and `python -m infograph.svc.main --port 8000` as the standard entrypoint.
- Health router exposed at `/api/v1/health` to return `{"status": "ok"}` for system checks alongside a pytest suite that keeps the route guarded.
- `start.sh` / `stop.sh` scripts that stop prior processes, spawn services in the background, write PID/log files, and expose a quick CLI intro for local development.
- `docker-compose.yml` that wires backend and frontend services with env_file references so secrets are never hard-coded, providing a standardized `docker compose up --build` experience.

## Prerequisites

- Python **3.11+** for the backend (install dependencies via `pip install -e backend/.[test]`).
- Node.js **20+** (or compatible manager) for the Vue 3 frontend workflow.
- Docker Engine **23.0+** and Docker Compose plugin if you prefer containerized workflows.

## Quick Start

### 1. Environment variables

Populate backend and frontend `.env` files before bootstrapping:

```bash
cat <<'EOF' > backend/.env
GOOGLE_CLIENT_ID=your-google-client-id
JWT_SECRET=your-jwt-secret
database_PATH=/workspace/data/duckdb
INFOGRAPHIC_PATH=/workspace/data/infographics
LOG_LEVEL=info
EOF

cat <<'EOF' > frontend/.env
VITE_API_BASE=http://localhost:8000
VITE_GOOGLE_CLIENT_ID=your-google-client-id
VITE_FRONTEND_PORT=3001
EOF
```

Replace the placeholders with values from your own Google OAuth setup and secrets store. The Docker Compose workflow reuses these files via its `env_file` entries.

### 2. Bootstrap services

```bash
chmod +x ./start.sh ./stop.sh
./start.sh
```

`start.sh` ensures old backend and frontend processes stop cleanly, writes logs to `./logs/backend.log` (and `./logs/frontend.log` once the UI is added), and tracks PIDs inside `./pids/backend.pid` / `./pids/frontend.pid`. After starting, it prints `Frontend URL: http://localhost:3001` so you know where to visit. Stop the running services with `./stop.sh`.

### 3. CLI quick intro

```bash
./start.sh                   # start backend + frontend, rotating logs/pids
./stop.sh                    # stop both services cleanly via stored PIDs
tail -f logs/backend.log      # watch backend logs (frontend logs once available)
python -m infograph.svc.main --port 8000  # run the backend directly via Click/uvicorn for debugging
```

### 4. Docker Compose alternative

```bash
docker compose up --build
```

The Compose file mounts the sources, installs dependencies inside the containers, and still reads environment values from `backend/.env` and `frontend/.env` so no secrets land in the YAML. Use `docker compose down` to stop all services and `docker compose logs backend` / `docker compose logs frontend` for diagnosis.

## Backend Setup

```bash
cd backend
pip install -e .[test]
python -m infograph.svc.main --port 8000
```

The FastAPI documentation is available at `/api/v1/docs` (Swagger) and `/api/v1/redoc` by default, and the health route sits at `/api/v1/health`.

## Testing

```bash
cd backend
pytest tests/test_health_router.py -q
```

Running the health endpoint test ensures `/api/v1/health` remains reachable as the project evolves. For broader coverage, `pytest tests` executes the full suite.

## Configuration

### backend/.env

```bash
GOOGLE_CLIENT_ID=your-google-client-id
JWT_SECRET=your-jwt-secret
DATABASE_PATH=/workspace/data/duckdb
INFOGRAPHIC_PATH=/workspace/data/infographics
LOG_LEVEL=info
```

### frontend/.env

```bash
VITE_API_BASE=http://localhost:8000
VITE_GOOGLE_CLIENT_ID=your-google-client-id
VITE_FRONTEND_PORT=3001
```

These env files are referenced by `start.sh`, `stop.sh`, and `docker-compose.yml` so you only need to configure them once locally before starting services.
