from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float

from database import Base


class PetStatus(Base):
    __tablename__ = "pet_status"

    id = Column(Integer, primary_key=True)
    status = Column(String)
