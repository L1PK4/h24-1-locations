from typing import Annotated
from fastapi import APIRouter, Depends

from service.domain.commands.paths import PathCommand
from service.domain.models.paths import Paths
from service.domain.views.paths import PathsView
from service.infrastructure.sqlalchemy.repository import (
    PathRepository,
    get_location_repository,
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
    repository: Annotated[PathRepository, Depends(get_location_repository)]
) -> list[PathsView]:
    result = await repository.get_all()
    return [PathsView.from_model(model) for model in result]


@router.post(
    "/paths",
    status_code=200,
    responses={200: {"description": "Path created", "model": PathsView}},
)
async def create_path(
    path: PathCommand,
    repository: Annotated[PathRepository, Depends(get_location_repository)],
) -> PathsView:
    result = await repository.add(
        Paths(lat=path.lat, lon=path.lon, type=path.type, name=path.name)
    )
    return PathsView.from_model(result)


@router.delete(
    "/paths/{entity_id}",
    status_code=200,
    responses={200: {"description": "Path deleted"}},
)
async def delete_path(
    entity_id: int,
    repository: Annotated[PathRepository, Depends(get_location_repository)],
) -> None:
    await repository.delete(entity_id)
