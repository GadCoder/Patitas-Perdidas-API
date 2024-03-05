from pydantic import BaseModel


class PetColorBase(BaseModel):
    color: str


class PetColorCreate(PetColorBase):
    pass


class PetColor(PetColorBase):
    id: int

    class Config:
        orm_mode = True