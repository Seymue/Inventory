from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from core.model.base import Base


class Category(Base):
    __tablename__ = "Category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    #Для иерархии категорий, опционально
    #parent_id = Column(Integer, ForeignKey('Category.id'), nullable=True)  # Может быть NULL для корневых категорий

    objects = relationship(
        "Object",
        back_populates="category"
    )

    #Для иерархии категорий, опционально?
    #Труктура иерархии
    #parent = relationship("Category", remote_side=[id])
    #children = relationship("Category")

