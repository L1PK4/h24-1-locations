from collections.abc import Sequence
from typing import Annotated
from fastapi import Depends
from sqlalchemy import delete, select
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

    async def delete(self, entity_id: int) -> None:
        q = delete(Locations).where(Locations.id == entity_id)
        await self.__session.execute(q)

    async def get_all(self) -> Sequence[Locations]:
        return (await self.__session.execute(select(Locations))).scalars().all()


async def get_repository(
    session: Annotated[AsyncSession, Depends(get_session)]
) -> LocationRepository:
    return LocationRepository(session)
