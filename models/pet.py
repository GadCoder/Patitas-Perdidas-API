from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from database import Base


class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    longitude = Column(float)
    latitude = Column(Float)
    district = Column(String)
    report_date = Column(DateTime)

    breed_id = Column(Integer, ForeignKey("pet_breeds.id"))
    status_id = Column(Integer, ForeignKey("pet_status.id"))
    pet_type_id = Column(Integer, ForeignKey("pet_types.id"))
    pet_color_id = Column(Integer, ForeignKey("pet_colors.id"))
    user_id = Column(Integer, ForeignKey="users.id")

    user = relationship("User", back_populates="pets")

