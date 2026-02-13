import os
from infograph.svc.api_router_base import APIRouterBase

from infograph.stores.duckdb.duckdb_client import DuckDBClient
from infograph.stores.duckdb.user_store_duckdb import UserStoreDuckDB
from infograph.services.auth_service import AuthService
from infograph.svc.api.v1.routers.health_router import HealthRouter
from infograph.svc.api.v1.routers.auth_router import create_auth_router


class ServiceAPIRouter(APIRouterBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize persistence and services
        db_path = os.environ.get("DATABASE_PATH", "/workspace/data/duckdb/infograph.db")
        client = DuckDBClient(db_path)
        user_store = UserStoreDuckDB(client)

        jwt_secret = os.environ.get("JWT_SECRET", "secret")
        google_client_id = os.environ.get("GOOGLE_CLIENT_ID", "")

        auth_service = AuthService(user_store, client_id=google_client_id, jwt_secret=jwt_secret)

        # Register routers
        self.health_router = HealthRouter()
        super().include_router(self.health_router, prefix="/health", tags=["Health"])  

        # Auth router
        self.auth_router = create_auth_router(auth_service)
        super().include_router(self.auth_router, prefix="", tags=["Auth"]) 
