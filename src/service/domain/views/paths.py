from typing import Self
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from service.domain.models.paths import Paths
from service.domain.views.locations import LocationView


class PathsView(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    id: int
    name: str
    description: str
    price: int
    picture_url: str | None = None
    locations: list[LocationView] = []

    @classmethod
    def from_model(cls, model: Paths, locations: list[LocationView]) -> Self:
        return cls(
            id=model.id,
            name=model.name,
            description=model.description,
            price=model.price,
            picture_url=model.picture_url,
            locations=locations,
        )
