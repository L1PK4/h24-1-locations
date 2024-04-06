from collections.abc import Sequence
from typing import Annotated
from fastapi import Depends
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from service.domain.models.paths import Paths
from service.domain.views.paths import PathsView
from service.infrastructure.sqlalchemy.session_manager import get_session


class PathRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.__session = session

    async def add(self, path: Paths) -> Paths:
        self.__session.add(path)
        await self.__session.flush()
        return path

    async def delete(self, entity_id: int) -> None:
        q = delete(Paths).where(Paths.id == entity_id)
        await self.__session.execute(q)

    # async def get_all(self) -> Sequence[PathsView]:
    #     stmt = select()
    # return (await self.__session.execute(select(Paths))).scalars().all()


async def get_path_repository(
    session: Annotated[AsyncSession, Depends(get_session)]
) -> PathRepository:
    return PathRepository(session)
