from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.model.base import Base


class Object(Base):
    __tablename__ = "objects"  # Исправлено на нижний регистр

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    inventory_number = Column(String(50), nullable=False)
    quantity = Column(Integer, nullable=False)
    comments = Column(String(1000), nullable=True)

    # Внешние ключи
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)

    # Связи
    category = relationship(
        "Category",
        back_populates="objects",
        lazy="selectin"
    )
    location = relationship(
        "Locations",
        back_populates="objects",
        lazy="selectin"
    )

    def __repr__(self):
        return f"<Object(id={self.id}, name='{self.name}', inv='{self.inventory_number}')>"