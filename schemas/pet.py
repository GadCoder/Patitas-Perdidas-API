from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PetBase(BaseModel):
    name: Optional[str] = None
    district: str
    report_date: datetime

class PetCreate(PetBase):
    breed_id: int
    status_id: int
    pet_type_id: int
    pet_color_id: int
    user_id: int

class Pet(PetBase):
    id: int
    breed_id: int
    status_id: int
    pet_type_id: int
    pet_color_id: int
    user_id: int

    class Config:
        orm_mode = True
