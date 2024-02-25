from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    names: str
    lastnames: str
    phone: str
    email: str

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserInDB(User):
    hashed_password: str


from .pet import Pet  # adjust import path accordingly

class UserWithPets(User):
    pets: List[Pet]

    class Config:
        orm_mode = True