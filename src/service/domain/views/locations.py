from typing import Self
from pydantic import BaseModel

from service.domain.models.locations import LocationType, Locations


class LocationView(BaseModel):
    id: int
    lat: float
    lon: float
    type: LocationType
    name: str
    picture_url: str | None = None

    @classmethod
    def from_model(cls, model: Locations) -> Self:
        return cls(
            id=model.id,
            lat=model.lat,
            lon=model.lon,
            type=model.type,
            name=model.name,
            picture_url=model.picture_url,
        )
