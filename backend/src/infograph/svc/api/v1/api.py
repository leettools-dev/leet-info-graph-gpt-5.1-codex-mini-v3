from fastapi import APIRouter

import os

from .routers.health_router import router as health_router
from .routers.auth_router import create_auth_router
from .routers.session_router import create_session_router
from infograph.services.auth_service import AuthService
from infograph.services.infographic_service import InfographicService
from infograph.stores.duckdb import DuckDBClient, SessionStoreDuckDB, UserStoreDuckDB, InfographicStoreDuckDB
from infograph.svc.api.v1.routers.infographic_router import create_infographic_router


class ServiceAPIRouter(APIRouter):
    def __init__(self) -> None:
        super().__init__()
        db_path = os.getenv("DATABASE_PATH", "./data/duckdb/infograph.db")
        client = DuckDBClient(db_path)
        user_store = UserStoreDuckDB(client)
        session_store = SessionStoreDuckDB(client)
        auth_service = AuthService(
            user_store=user_store,
            client_id=os.getenv("GOOGLE_CLIENT_ID", ""),
            jwt_secret=os.getenv("JWT_SECRET", "secret"),
        )
        self.include_router(health_router, prefix="/api/v1", tags=["Health"])
        self.include_router(create_auth_router(auth_service), prefix="/api/v1", tags=["Auth"])
        self.include_router(
            create_session_router(auth_service, session_store),
            prefix="/api/v1",
            tags=["Sessions"],
        )
        # Infographic router and service
        infographic_store = InfographicStoreDuckDB(client)
        infographic_service = InfographicService(infographic_store)
        self.include_router(
            create_infographic_router(auth_service, infographic_service, infographic_store),
            prefix="/api/v1",
            tags=["Infographic"],
        )
