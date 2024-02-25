from pydantic import BaseModel


class PetMediaBase(BaseModel):
    media_url: str
    pet_id: int

class PetMedia(PetMediaBase):
    id: int

    class Config:
        orm_mode = True 