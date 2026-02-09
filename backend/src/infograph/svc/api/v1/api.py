from fastapi import APIRouter

import os

from .routers.health_router import router as health_router
from .routers.auth_router import create_auth_router
from infograph.services.auth_service import AuthService
from infograph.stores.in_memory_user_store import InMemoryUserStore


class ServiceAPIRouter(APIRouter):
    def __init__(self) -> None:
        super().__init__()
        user_store = InMemoryUserStore()
        auth_service = AuthService(
            user_store=user_store,
            client_id=os.getenv("GOOGLE_CLIENT_ID", ""),
            jwt_secret=os.getenv("JWT_SECRET", "secret"),
        )
        self.include_router(health_router, prefix="/api/v1", tags=["Health"])
        self.include_router(create_auth_router(auth_service), prefix="/api/v1", tags=["Auth"])
