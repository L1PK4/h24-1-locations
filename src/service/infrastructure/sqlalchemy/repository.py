from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from service.models.locations import Locations


class LocationRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.__session = session

    async def add(self, location: Locations) -> Locations:
        self.__session.add(location)
        await self.__session.flush()
        return location

    async def get_all(self) -> list[Locations]:
        return (await self.__session.execute(select(Locations))).mappings().all()
