#core.model.locations.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.model.base import Base


class Locations(Base):
    __tablename__ = "locations"  # Исправлено на нижний регистр

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_2022 = Column(String(100), nullable=False)

    objects = relationship(
        "Object",
        back_populates="location",
        lazy="selectin"
    )

    def __repr__(self):
        return f"<Location(id={self.id}, name='{self.name_2022}')>"