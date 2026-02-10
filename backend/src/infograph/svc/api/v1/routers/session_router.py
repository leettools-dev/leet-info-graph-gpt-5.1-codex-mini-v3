from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError

from infograph.core.schemas.research_session import ResearchSession, ResearchSessionCreate
from infograph.core.schemas.user import User
from infograph.services.auth_service import AuthService
from infograph.stores.abstract_session_store import AbstractSessionStore


bearer = HTTPBearer(auto_error=True)


def _build_current_user_dependency(auth_service: AuthService):
    async def _get_current_user(
        token: HTTPAuthorizationCredentials = Security(bearer),
    ) -> User:
        try:
            return auth_service.get_user_from_token(token.credentials)
        except (JWTError, ValueError) as exc:
            raise HTTPException(status_code=401, detail="Invalid or expired token") from exc

    return _get_current_user


def create_session_router(
    auth_service: AuthService,
    session_store: AbstractSessionStore,
) -> APIRouter:
    """Create router and dependencies for research session CRUD functionality."""
    router = APIRouter()
    get_current_user = _build_current_user_dependency(auth_service)

    @router.post("/sessions", response_model=ResearchSession, status_code=200)
    async def create_session(
        payload: ResearchSessionCreate,
        current_user: User = Depends(get_current_user),
    ) -> ResearchSession:
        return session_store.create_session(current_user.user_id, payload)

    @router.get("/sessions", response_model=list[ResearchSession])
    async def list_sessions(
        limit: int = Query(10, ge=1, le=100),
        offset: int = Query(0, ge=0),
        current_user: User = Depends(get_current_user),
    ) -> list[ResearchSession]:
        sessions = session_store.list_sessions(current_user.user_id, limit=limit, offset=offset)
        return list(sessions)

    @router.get("/sessions/{session_id}", response_model=ResearchSession)
    async def get_session(
        session_id: str,
        current_user: User = Depends(get_current_user),
    ) -> ResearchSession:
        session = session_store.get_session(session_id)
        if not session or session.user_id != current_user.user_id:
            raise HTTPException(status_code=404, detail="Session not found")
        return session

    @router.delete("/sessions/{session_id}")
    async def delete_session(
        session_id: str,
        current_user: User = Depends(get_current_user),
    ) -> dict[str, bool]:
        session = session_store.get_session(session_id)
        if not session or session.user_id != current_user.user_id:
            raise HTTPException(status_code=404, detail="Session not found")
        success = session_store.delete_session(session_id)
        return {"success": success}

    return router
