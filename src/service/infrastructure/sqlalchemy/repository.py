from typing import Annotated
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from service.domain.models.locations import Locations
from service.infrastructure.sqlalchemy.session_manager import get_session


class LocationRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.__session = session

    async def add(self, location: Locations) -> Locations:
        self.__session.add(location)
        await self.__session.flush()
        return location

    async def get_all(self) -> list[Locations]:
        return (await self.__session.execute(select(Locations))).mappings().all()


async def get_repository(
    session: Annotated[AsyncSession, Depends(get_session)]
) -> LocationRepository:
    return LocationRepository(session)
