from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from service.domain.views.locations import LocationView
from service.infrastructure.sqlalchemy.repository import (
    LocationRepository,
    get_repository,
)
from service.infrastructure.sqlalchemy.session_manager import get_session

router = APIRouter(prefix="/api/v1")


@router.get("/")
async def index(session: Annotated[AsyncSession, Depends(get_session)]):
    res = await session.execute(text("SELECT 1"))
    return {"message": "Hello World", "result": res.fetchone()[0]}


@router.get(
    "/locations",
    response_model=list[LocationView],
    responses={
        200: {"model": list[LocationView], "description": "List of locations"},
    },
)
async def get_locations(
    repository: Annotated[LocationRepository, Depends(get_repository)]
) -> list[LocationView]:
    return [loc.to_view(LocationView) for loc in (await repository.get_all())]
