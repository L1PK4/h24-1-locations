from pydantic import BaseModel

from service.domain.models.locations import LocationType


class LocationCommand(BaseModel):
    lat: float
    lon: float
    type: LocationType
    name: str | None = None
