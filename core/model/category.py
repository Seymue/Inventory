#core.model.category.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from core.model.base import Base


class Category(Base):
    __tablename__ = "categories"  # Исправлено на нижний регистр

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    objects = relationship(
        "Object",
        back_populates="category",
        lazy="selectin"
    )

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"