import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.v1.api import ServiceAPIRouter


API_VERSION = "1.0.0"
DEFAULT_ALLOWED_ORIGINS = [
    "http://localhost:3001",
    "http://127.0.0.1:3001",
]


def _get_allowed_origins() -> list[str]:
    env_value = os.getenv("API_CORS_ALLOWED_ORIGINS")
    if not env_value:
        return list(DEFAULT_ALLOWED_ORIGINS)

    parsed = [origin.strip() for origin in env_value.split(",") if origin.strip()]
    return parsed or list(DEFAULT_ALLOWED_ORIGINS)



def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="Infograph Assistant API",
        version=API_VERSION,
        docs_url="/api/v1/docs",
        redoc_url="/api/v1/redoc",
        openapi_url="/api/v1/openapi.json",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=_get_allowed_origins(),
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
        allow_headers=["*"],
    )

    @app.get("/", include_in_schema=False)
    async def root() -> dict[str, str]:
        return {"status": "running", "version": API_VERSION}

    router = ServiceAPIRouter()
    app.include_router(router)

    return app
