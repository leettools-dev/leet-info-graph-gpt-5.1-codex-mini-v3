# Session Management

Implement backend and frontend pieces for research session CRUD:

- Backend: Create `session_router.py` with all session endpoints (/sessions)
- Backend: Implement `SessionStoreDuckDB` store (create/list/get/delete)
- Backend: Wire session router into ServiceAPIRouter
- Tests: Add pytest tests for session router and store (happy path, pagination, delete)

Environment variables:
- DATABASE_PATH

Bootstrap requirements:
- start.sh/stop.sh present at repo root (already satisfied)
- README updated with quick start (already present)
