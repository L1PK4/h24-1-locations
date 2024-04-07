from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from service.domain.models.paths import Paths


class PathCommand(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    name: str
    description: str
    price: int

    location_ids: list[int]

    def to_model(self) -> Paths:
        return Paths(
            name=self.name,
            description=self.description,
            price=self.price,
            location_ids=self.location_ids,
        )
