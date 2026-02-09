from fastapi import APIRouter

from .routers.health_router import router as health_router


class ServiceAPIRouter(APIRouter):
    def __init__(self) -> None:
        super().__init__()
        self.include_router(health_router, prefix="/api/v1", tags=["Health"])
