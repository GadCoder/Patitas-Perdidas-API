from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float

from database import Base


class PetColor(Base):
    __tablename__ = "pet_colors"

    id = Column(Integer, primary_key=True)
    color = Column(String)
