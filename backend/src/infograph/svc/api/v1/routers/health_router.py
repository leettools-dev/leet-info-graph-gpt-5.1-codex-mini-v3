from infograph.svc.api_router_base import APIRouterBase

class HealthRouter(APIRouterBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        @self.get("/", summary="Service health")
        async def health():
            return {"status": "healthy"}
