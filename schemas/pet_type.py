from pydantic import BaseModel


class PetTypeBase(BaseModel):
    name: str
    description: str



class Pet(PetTypeBase):
    id: int

    class Config:
        orm_mode = True