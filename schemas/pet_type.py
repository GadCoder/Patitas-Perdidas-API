from pydantic import BaseModel


class PetTypeBase(BaseModel):
    description: str



class Pet(PetTypeBase):
    id: int

    class Config:
        orm_mode = True