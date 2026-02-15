from fastapi import APIRouter, Request

class APIRouterBase(APIRouter):
    """Base class for API routers providing access to common dependencies."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def get_locale(self, request: Request) -> str:
        accept_language = request.headers.get("Accept-Language", "en-US")
        return accept_language.split(",")[0].strip()
