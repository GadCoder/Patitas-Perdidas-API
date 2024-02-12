from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float

from database import Base


class PetBreed(Base):
    __tablename__ = "pet_breeds"

    id = Column(Integer, primary_key=True)
    breed = Column(String)
