from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from db.base_class import Base


class PetType(Base):
    id = Column(Integer, primary_key=True)
    description = Column(String)
