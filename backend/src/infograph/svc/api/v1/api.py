from infograph.svc.api_router_base import APIRouterBase


class ServiceAPIRouter(APIRouterBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        from infograph.svc.api.v1.routers.health_router import health_router

        self.include_router(
            health_router,
            prefix="/health",
            tags=["Health"],
        )
