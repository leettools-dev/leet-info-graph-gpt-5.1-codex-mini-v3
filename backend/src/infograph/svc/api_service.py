from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    app = FastAPI(
        title="Infograph Assistant API",
        version="0.1.0",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
    )

    # CORS - allow localhost origins by default for development
    origins = ["http://localhost", "http://localhost:3000", "http://localhost:5173"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    # Register routers
    from infograph.svc.api.v1.api import ServiceAPIRouter
    api_router = ServiceAPIRouter()
    app.include_router(api_router, prefix="/api/v1")

    @app.get("/")
    async def root():
        return {"status": "ok", "service": "infograph"}

    return app


# Export a module-level `app` for tools that import the app directly (uvicorn_runner, CLI imports)
app = create_app()
