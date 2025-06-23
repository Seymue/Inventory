from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from core.model.base import Base


class Object(Base):
    __tablename__ = "Object"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    inventory_number = Column(Integer, nullable=False)

    # Внешние ключи
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)

    # сomments = Column(String(1000), nullable=True)

# Связи
    category = relationship(
        "Category",
        back_populates="objects",
        lazy="selectin"#для оптимизации запроса
    )
    location = relationship(
        "Location",
        back_populates="objects",
        lazy="selectin"
    )
