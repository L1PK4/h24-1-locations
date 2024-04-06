from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from service.domain.models.locations import LocationType


class LocationCommand(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    lat: float
    lon: float
    type: LocationType
    name: str | None = None
