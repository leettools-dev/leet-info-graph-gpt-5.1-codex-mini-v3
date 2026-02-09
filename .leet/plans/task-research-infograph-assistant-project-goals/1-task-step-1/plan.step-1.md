---
task_name: step-1
status: in_progress
created_at: '2026-02-09T10:28:50Z'
updated_at: '2026-02-09T17:47:30Z'
---

# Task: step-1

## Description

Tasks:**

## Implementation Plan

1. Bootstrap the workspace by documenting required environment variables, and adding `start.sh`/`stop.sh` scripts that manage PID files, logs, and print the frontend URL as part of the new Quick Start experience.
2. Build the backend skeleton: create the `backend/src/infograph` package, `svc` structure, Click CLI entry point, FastAPI app with CORS, and the health router under `/api/v1/health`.
3. Add `pyproject.toml` with the required dependencies and implement pytest coverage for the health endpoint to validate the new router.
4. Update project documentation (README) with the quick start instructions, feature summary, and testing guidance so the bootstrap is exposed to developers.

