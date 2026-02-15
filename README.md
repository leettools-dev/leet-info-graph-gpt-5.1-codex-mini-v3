# leet-info-graph-gpt-5.1-codex-mini-v3

> This project is being developed by an autonomous coding agent.

## Overview

The Research Infograph Assistant is a full-stack experiment that lets users sign in with Google, submit research prompts, and receive AI-generated infographics powered by FastAPI, Vue 3, DuckDB, and TailwindCSS. This repository focuses on the backend service skeleton, its supporting CLI, and the tooling needed to validate the `/api/v1/health` endpoint during early development.

## Features

- Documented the backend dependency graph in `backend/pyproject.toml`, including FastAPI, Click, DuckDB, Google OAuth helpers, and pytest support so the service, CLI, and tests install consistently.
- Added `start.sh`/`stop.sh` plus PID/log management and a CLI quick intro so the backend and frontend can be bootstrapped together locally.
- Introduced a minimal `docker-compose.yml` so the services can be started with `docker compose up --build`, wiring environment variables through env_file references instead of hardcoding secrets.
- Added backend FastAPI service outline for the Research Infograph Assistant.

## Prerequisites

- Python **3.11+** for the FastAPI backend (pip with editable installs).
- Node.js **20+** and npm or yarn for the Vue frontend.
- Docker Engine **23.0+** + Docker Compose plugin if you plan to use the Docker workflow.

## Quick Start

### 1. Prepare environment variables

Create the backend and frontend env files before starting either workflow:

```bash
cat <<'EOF' > backend/.env
GOOGLE_CLIENT_ID=your-google-client-id
JWT_SECRET=your-jwt-secret
DATABASE_PATH=/workspace/data/duckdb
INFOGRAPHIC_PATH=/workspace/data/infographics
LOG_LEVEL=info
EOF
- Node.js and npm (v16+)
- Python 3.11
- Environment variables documented in the backend and frontend sections below.
### Quick Start

1. Environment variables
   ```bash
GOOGLE_CLIENT_ID=your-google-client-id
JWT_SECRET=your-jwt-secret
DATABASE_PATH=/workspace/data/duckdb
INFOGRAPHIC_PATH=/workspace/data/infographics
LOG_LEVEL=info

VITE_API_BASE=http://localhost:8000
VITE_GOOGLE_CLIENT_ID=your-google-client-id
VITE_FRONTEND_PORT=3001
```

2. Bootstrap services
   ```bash
   chmod +x ./start.sh ./stop.sh
   ./start.sh
   ```
   - Logs: `./logs/backend.log` & `./logs/frontend.log`
   - PIDs: `./pids/backend.pid`, `./pids/frontend.pid`
   - `start.sh` stops existing processes, runs backend and frontend in background, and writes PID/log files.
   - After startup, `start.sh` prints `Frontend available at http://localhost:3001`

cat <<'EOF' > frontend/.env
VITE_API_BASE=http://localhost:8000
VITE_GOOGLE_CLIENT_ID=your-google-client-id
VITE_FRONTEND_PORT=3001
EOF
```

These same files are referenced by the Docker Compose env_file blocks below, so you can reuse them when containerizing.

### 2. Local CLI bootstrap

```bash
chmod +x ./start.sh ./stop.sh
./start.sh    # launches backend + frontend, writes logs/pids, prints Frontend URL
```

- Logs are streamed to `./logs/backend.log` and `./logs/frontend.log`.
- PIDs are tracked in `./pids/backend.pid` and `./pids/frontend.pid` so the `stop.sh` script can kill them reliably.
- The backend listens on `http://localhost:8000` and exposes the health route at `/api/v1/health`.

### 3. Docker Compose alternative

```bash
docker compose up --build
```

- The services share your local source tree via bind mounts so code edits appear instantly.
- Environment values are loaded from `backend/.env` and `frontend/.env`; there are no secrets in `docker-compose.yml` itself.
- Visit `http://localhost:3001` once the frontend is ready; it will call the backend health route to verify connectivity.
- Use `docker compose down` to stop both services and `docker compose logs backend` to inspect the backend output.

### CLI quick intro

```bash
./start.sh         # start backend & frontend via CLI helpers
./stop.sh          # stop running services
tail -f logs/*.log # monitor backend and frontend logs
```

## Backend Setup

```bash
cd backend
pip install -e .[test]
python -m infograph.svc.main --port 8000
```

The backend exposes documentation at `/api/v1/docs` and `/api/v1/redoc`, and the health route lives at `/api/v1/health`.

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Once the frontend server is running (by default on port 3001), it will ping the backend health endpoint to show the connection state.

## Configuration

### Backend

Create `backend/.env` with:

```
GOOGLE_CLIENT_ID=your-google-client-id
JWT_SECRET=your-jwt-secret
DATABASE_PATH=/workspace/data/duckdb
INFOGRAPHIC_PATH=/workspace/data/infographics
LOG_LEVEL=info
```

### Frontend

Create `frontend/.env` with:

```
VITE_API_BASE=http://localhost:8000
VITE_GOOGLE_CLIENT_ID=your-google-client-id
VITE_FRONTEND_PORT=3001
```

## Testing

The backend test suite covers the FastAPI health endpoint and can be run independently:

```bash
cd backend
pytest tests/test_health_router.py -q
```

`pytest` loads `infograph.svc.api_service.create_app()` so the `/api/v1/health` route stays validated as other features are added.
- Backend: `cd backend && pytest tests`
- Frontend: `cd frontend && npm run test`
