from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    names = Column(String)
    lastnames = Column(String)
    phone = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    pets = relationship("pets", back_populates="user")
