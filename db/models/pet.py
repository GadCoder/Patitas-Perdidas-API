from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from db.base_class import Base


class Pet(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    longitude = Column(Float)
    latitude = Column(Float)
    district = Column(String)
    report_date = Column(DateTime)

    breed_id = Column(Integer, ForeignKey("petbreed.id"))
    status_id = Column(Integer, ForeignKey("petstatus.id"))
    pet_type_id = Column(Integer, ForeignKey("pettype.id"))
    pet_color_id = Column(Integer, ForeignKey("petcolor.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="pets")

