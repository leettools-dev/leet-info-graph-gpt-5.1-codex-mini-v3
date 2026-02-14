Research Infograph Assistant

## Features

- Frontend: Google OAuth login page (LoginPage.vue), Pinia auth store, composable useAuth, router auth guards, and unit tests for auth store.
- Backend: Minimal FastAPI backend with health endpoint, Click CLI entrypoint, CORS setup, and start/stop scripts.

## Quick Start
Prerequisites:
- Python 3.11+
- Install dev deps: pip install -e backend/

Environment variables (backend/.env):
```
GOOGLE_CLIENT_ID=your-google-client-id
JWT_SECRET=your-jwt-secret
DATABASE_PATH=/workspace/data/duckdb
INFOGRAPHIC_PATH=/workspace/data/infographics
LOG_LEVEL=info
```

Start services:
- ./start.sh
Stop services:
- ./stop.sh

Frontend URL (if running): http://localhost:3001

CLI:
- python -m infograph.svc.main --port 8000
