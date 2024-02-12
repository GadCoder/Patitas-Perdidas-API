from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float

from database import Base


class PetColor(Base):
    __tablename__ = "pet_media"

    id = Column(Integer, primary_key=True)
    pet_id = Column(Integer, ForeignKey("pets.id"))
    media_url = Column(String)
