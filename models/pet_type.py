from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float

from database import Base


class PetType(Base):
    __tablename__ = "pet_types"

    id = Column(Integer, primary_key=True)
    pet_type = Column(String)
