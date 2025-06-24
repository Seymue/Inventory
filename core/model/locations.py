from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.model.base import Base


class Locations(Base):
    __tablename__ = "Locations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_2022 = Column(String(100), nullable=False)

    objects = relationship(
        "Object",
        back_populates="location",
        lazy="selectin"
    )
