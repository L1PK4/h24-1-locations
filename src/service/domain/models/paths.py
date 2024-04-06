from service.domain.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

from service.domain.models.locations import Locations


class Paths(BaseModel):
    __tablename__ = "paths"

    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    picture_url: Mapped[str | None]

    location_ids: Mapped[list[int]]
