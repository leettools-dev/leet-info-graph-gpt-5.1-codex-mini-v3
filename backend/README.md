# Infograph Backend

## Features
- Minimal FastAPI backend with health endpoint
- Google OAuth authentication (server-side verification + JWT generation)

## Quick Start

Prerequisites:
- Python 3.11+
- Install dependencies: poetry install (if using Poetry) or pip install -r requirements.txt

Environment variables (examples):
- GOOGLE_CLIENT_ID - Google OAuth client ID for verifying tokens (or GOOGLE_OAUTH_CLIENT_ID)
- JWT_SECRET - Secret key for signing JWT tokens
- DATABASE_PATH - Path to DuckDB database file (e.g. /workspace/data/duckdb/infograph.db)
- INFOGRAPHIC_PATH - Filesystem path to store generated infographic images
- LOG_LEVEL - Logging level (info, debug, warn)

Start the backend (development):

# Start via helper script (recommended)
./start.sh

# Or run directly with the CLI entrypoint
python -m infograph.svc.main --port 8000

Stop the backend:

./stop.sh

Logs are written to backend/backend.log and PID to backend/backend.pid

API docs available at http://localhost:8000/api/docs

CLI
- Start server with: python -m infograph.svc.main --port 8000

Health endpoint
- GET http://localhost:8000/api/v1/health -> {"status": "ok", "version": "1.0.0"}
