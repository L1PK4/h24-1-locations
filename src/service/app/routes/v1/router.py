from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from service.infrastructure.sqlalchemy.session_manager import get_session

router = APIRouter(prefix="/api/v1")


@router.get("/")
async def index(session: Annotated[AsyncSession, Depends(get_session)]):
    return {"message": "Hello World"}
