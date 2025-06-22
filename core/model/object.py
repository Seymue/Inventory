from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from core.model.base import Base
class Object(Base):
    __tablename__ = "object"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    inventory_number = Column(Integer, nullable=False)
    category = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    #сomments = Column(String(1000), nullable=True)

