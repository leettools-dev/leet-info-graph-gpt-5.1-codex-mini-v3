from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from infograph.svc.api.v1.api import ServiceAPIRouter


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="Research Infograph Assistant",
        description="Backend service for the Research Infograph Assistant application.",
        version="0.1.0",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    api_router = ServiceAPIRouter()
    app.include_router(api_router, prefix="/api/v1")

    @app.get("/health")
    async def root_health() -> dict:
        return {"status": "ok"}

    return app


app = create_app()
