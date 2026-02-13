from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError

from infograph.services.auth_service import AuthService
from infograph.services.infographic_service import InfographicService
from infograph.stores.abstract_infographic_store import AbstractInfographicStore

bearer = HTTPBearer(auto_error=True)


def _build_current_user_dependency(auth_service: AuthService):
    async def _get_current_user(token: HTTPAuthorizationCredentials = Depends(bearer)):
        try:
            return auth_service.get_user_from_token(token.credentials)
        except (JWTError, ValueError) as exc:
            raise HTTPException(status_code=401, detail="Invalid or expired token") from exc

    return _get_current_user


def create_infographic_router(
    auth_service: AuthService,
    infographic_service: InfographicService,
    infographic_store: AbstractInfographicStore,
) -> APIRouter:
    router = APIRouter()
    get_current_user = _build_current_user_dependency(auth_service)

    @router.get("/sessions/{session_id}/infographic")
    async def get_infographic(session_id: str, current_user=Depends(get_current_user)):
        infographic = infographic_store.get_infographic(session_id)
        if infographic is None:
            raise HTTPException(status_code=404, detail="Infographic not found")
        return infographic

    @router.get("/sessions/{session_id}/infographic/image")
    async def get_infographic_image(session_id: str, current_user=Depends(get_current_user)):
        infographic = infographic_store.get_infographic(session_id)
        if infographic is None:
            raise HTTPException(status_code=404, detail="Infographic not found")
        return FileResponse(infographic.image_path, media_type="image/png")

    return router
