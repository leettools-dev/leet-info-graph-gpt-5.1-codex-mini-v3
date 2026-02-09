# leet-info-graph-gpt-5.1-codex-mini-v3

> This project is being developed by an autonomous coding agent.

## Overview

The Research Infograph Assistant is a full-stack experiment that lets users sign in with Google, submit research prompts, and receive AI-generated infographics powered by FastAPI, Vue 3, DuckDB, and TailwindCSS. This repository contains the backend service skeleton and test coverage for the early health-check endpoint.

## Features

- Added README instructions covering quick start scripts, logs/pids, and backend health check usage.
## Getting Started

### Prerequisites

- Documented env as above?
### Quick Start

1. Environment variables
   ```bash
cat <<'EOF' > backend/.env
GOOGLE_CLIENT_ID=your-google-client-id
JWT_SECRET=your-jwt-secret
DATABASE_PATH=/workspace/data/duckdb
INFOGRAPHIC_PATH=/workspace/data/infographics
LOG_LEVEL=info
EOF

cat <<'EOF' > frontend/.env
VITE_API_BASE=http://localhost:8000
VITE_GOOGLE_CLIENT_ID=your-google-client-id
VITE_FRONTEND_PORT=3001
EOF
```

2. Bootstrap services
   ```bash
   chmod +x ./start.sh ./stop.sh
   ./start.sh
   ```
   - Logs: `./logs/backend.log` & `./logs/frontend.log`
   - PIDs: `./pids/backend.pid`, `./pids/frontend.pid`
   - After startup, `start.sh` prints `Frontend available at http://localhost:3001`

3. CLI quick intro
   ```bash
   ./start.sh         # start backend and frontend
   ./stop.sh          # stop running services
   tail -f logs/*.log # inspect backend/frontend logs
   ```

### Backend Setup

```bash
cd backend
pip install -e .[test]
python -m infograph.svc.main --port 8000
```

The service listens on `0.0.0.0:8000` and exposes the health route under `/api/v1/health`.

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Once the frontend server is running, it can call the backend health endpoint to confirm connectivity.

## Configuration

### Backend

Create a `.env` file with the following values before production runs:

```
GOOGLE_CLIENT_ID=your-google-client-id
JWT_SECRET=your-jwt-secret
DATABASE_PATH=/workspace/data/duckdb
INFOGRAPHIC_PATH=/workspace/data/infographics
LOG_LEVEL=info
```

### Frontend

Set the client-side environment variables when running the UI:

```
VITE_API_BASE=http://localhost:8000
VITE_GOOGLE_CLIENT_ID=your-google-client-id
VITE_FRONTEND_PORT=3001
```

## Testing

### Testing

Backend tests ensure the health endpoint behaves as expected:

```bash
cd backend
pytest tests/test_health_router.py -q
```

`pytest` loads the FastAPI app via `infograph.svc.api_service.create_app` to keep the `/api/v1/health` router verified while features evolve.
