from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from service.domain.models.locations import LocationType, Locations


class LocationCommand(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    lat: float
    lon: float
    type: LocationType
    name: str | None = None
    picture_url: str | None = None

    def to_model(self) -> Locations:
        return Locations(
            lat=self.lat,
            lon=self.lon,
            type=self.type,
            name=self.name,
            picture_url=self.picture_url,
        )
