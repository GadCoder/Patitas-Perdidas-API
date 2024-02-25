from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from db.base_class import Base

class PetBreed(Base):
    id = Column(Integer, primary_key=True)
    breed = Column(String)
    pet_type_id = Column(Integer, ForeignKey("pettype.id"))
