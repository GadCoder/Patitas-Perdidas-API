from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from db.base_class import Base

class PetMedia(Base):
    id = Column(Integer, primary_key=True)
    pet_id = Column(Integer, ForeignKey("pet.id"))
    media_url = Column(String)
