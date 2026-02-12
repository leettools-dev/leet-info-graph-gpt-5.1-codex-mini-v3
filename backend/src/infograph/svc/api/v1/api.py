from infograph.svc.api_router_base import APIRouterBase

class ServiceAPIRouter(APIRouterBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Register routers
        from infograph.svc.api.v1.routers.health_router import HealthRouter

        self.health_router = HealthRouter()
        super().include_router(self.health_router, prefix="/health", tags=["Health"]) 
