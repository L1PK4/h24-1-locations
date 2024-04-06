from enum import Enum

from sqlalchemy import String
from .base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column


class LocationType(str, Enum):
    HUB = "hub"
    PITSTOP = "pitstop"
    ATTRACTION = "attraction"
    RESORT = "resort"


class Locations(BaseModel):
    lat: Mapped[float]
    lon: Mapped[float]

    type: Mapped[LocationType] = mapped_column("type", String(30))
    name: Mapped[str]

    picture_url: Mapped[str]
