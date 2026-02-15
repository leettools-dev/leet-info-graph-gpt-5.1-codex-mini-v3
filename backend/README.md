# Infograph Backend

## Features
- Minimal FastAPI backend with health endpoint

## Quick Start

Prerequisites:
- Python 3.11+
- Install dependencies: poetry install (if using Poetry) or pip install -r requirements.txt

Environment variables:
- GOOGLE_OAUTH_CLIENT_ID - Google OAuth client ID (placeholder)
- JWT_SECRET - Secret key for signing JWT tokens

Start the backend:

./start.sh

Stop the backend:

./stop.sh

Logs are written to backend/backend.log and PID to backend/backend.pid

API docs available at http://localhost:8000/api/docs

CLI
- Start server with: python -m infograph.svc.main --port 8000
