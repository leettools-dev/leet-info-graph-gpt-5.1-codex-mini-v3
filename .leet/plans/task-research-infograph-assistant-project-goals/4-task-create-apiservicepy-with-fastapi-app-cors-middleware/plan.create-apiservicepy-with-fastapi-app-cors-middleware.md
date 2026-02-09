---
task_name: create-apiservicepy-with-fastapi-app-cors-middleware
status: in_progress
created_at: '2026-02-09T10:28:50Z'
updated_at: '2026-02-09T23:10:00Z'
---

# Task: create-apiservicepy-with-fastapi-app-cors-middleware

## Description

Create `api_service.py` with FastAPI app, CORS middleware

## Plan

1. Confirm the API router aggregator currently registers the `/api/v1/health` router and plan how to include it in the new app.
2. Implement an `_get_allowed_origins` helper to parse `API_CORS_ALLOWED_ORIGINS` or fall back to the default localhost frontend URLs.
3. Initialize the FastAPI app with proper metadata, versioned docs paths under `/api/v1`, and attach the CORS middleware using the helper.
4. Add the root `/` endpoint for a simple status check, include `ServiceAPIRouter`, and ensure middleware evaluation happens before routes.
