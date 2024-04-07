from typing import Annotated
from fastapi import APIRouter, Depends

from service.domain.commands.locations import LocationCommand
from service.domain.models.locations import Locations
from service.domain.views.locations import LocationView
from service.infrastructure.sqlalchemy.repository import (
    LocationRepository,
    get_location_repository,
)

router = APIRouter(prefix="/api/v1")


@router.get(
    "/locations",
    response_model=list[LocationView],
    responses={
        200: {"model": list[LocationView], "description": "List of locations"},
    },
)
async def get_locations(
    repository: Annotated[LocationRepository, Depends(get_location_repository)]
) -> list[LocationView]:
    result = await repository.get_all()
    return [LocationView.from_model(model) for model in result]


@router.post(
    "/locations",
    status_code=200,
    responses={200: {"description": "Location created", "model": LocationView}},
)
async def create_location(
    location: LocationCommand,
    repository: Annotated[LocationRepository, Depends(get_location_repository)],
) -> LocationView:
    result = await repository.add(location.to_model())
    return LocationView.from_model(result)


@router.delete(
    "/locations/{entity_id}",
    status_code=200,
    responses={200: {"description": "Location deleted"}},
)
async def delete_location(
    entity_id: int,
    repository: Annotated[LocationRepository, Depends(get_location_repository)],
) -> None:
    await repository.delete(entity_id)
