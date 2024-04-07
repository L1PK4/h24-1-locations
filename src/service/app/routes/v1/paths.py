from typing import Annotated
from fastapi import APIRouter, Depends

from service.domain.commands.paths import PathCommand
from service.domain.models.paths import Paths
from service.domain.views.paths import PathsView
from service.infrastructure.sqlalchemy.path_repository import (
    PathRepository,
    get_path_repository,
)

router = APIRouter(prefix="/api/v1")


@router.get(
    "/paths",
    response_model=list[PathsView],
    responses={
        200: {"model": list[PathsView], "description": "List of paths"},
    },
)
async def get_paths(
    repository: Annotated[PathRepository, Depends(get_path_repository)]
) -> list[PathsView]:
    result = await repository.get_all()
    return list(result)


@router.post(
    "/paths",
    status_code=200,
    responses={200: {"description": "Path created", "model": PathsView}},
)
async def create_path(
    path: PathCommand,
    repository: Annotated[PathRepository, Depends(get_path_repository)],
) -> PathsView:
    result = await repository.add(path.to_model())

    return PathsView.from_model(result, [])


@router.delete(
    "/paths/{entity_id}",
    status_code=200,
    responses={200: {"description": "Path deleted"}},
)
async def delete_path(
    entity_id: int,
    repository: Annotated[PathRepository, Depends(get_path_repository)],
) -> None:
    await repository.delete(entity_id)
