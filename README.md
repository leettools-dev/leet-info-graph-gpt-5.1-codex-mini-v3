# leet-info-graph-gpt-5.1-codex-mini-v3

> This project is being developed by an autonomous coding agent.

## Overview

The Research Infograph Assistant is a full-stack experiment that lets users sign in with Google, submit research prompts, and receive AI-generated infographics powered by FastAPI, Vue 3, DuckDB, and TailwindCSS. This repository contains the backend service skeleton and test coverage for the early health-check endpoint.

## Features

- Backend skeleton with FastAPI service, CORS middleware, and Click CLI entry point
- `/api/v1/health` endpoint returning status and version information
## Getting Started

### Prerequisites

- Python 3.11+ to run the backend service and tests.
- Node 18+ and npm 10+ for the frontend development server (future work).

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

Backend tests ensure the health endpoint behaves as expected:

```bash
cd backend
pytest tests/test_health_router.py -q
```

The suite exercises `infograph.svc.api_service.create_app` and the `/api/v1/health` router to keep the core skeleton stable as features are added.
