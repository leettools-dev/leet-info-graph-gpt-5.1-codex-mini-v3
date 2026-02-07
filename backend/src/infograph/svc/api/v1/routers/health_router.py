from infograph.svc.api_router_base import APIRouterBase


health_router = APIRouterBase()


@health_router.get("", response_model=dict)
async def health_check() -> dict:
    return {"status": "ok", "version": "1.0.0"}
