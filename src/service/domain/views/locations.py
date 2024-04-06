from pydantic import BaseModel

from service.domain.models.locations import LocationType


class LocationView(BaseModel):
    id: int
    lat: float
    lon: float
    type: LocationType
    name: str
