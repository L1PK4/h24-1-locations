from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class PathCommand(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    name: str
    description: str
    price: int

    location_ids: list[int]
