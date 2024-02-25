from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from db.base_class import Base


class PetStatus(Base):
    id = Column(Integer, primary_key=True)
    status = Column(String)
