from pydantic import BaseModel


class PetColorBase(BaseModel):
    name: str
    color_name: str


class PetColorCreate(PetColorBase):
    pass


class PetColor(PetColorBase):
    id: int

    class Config:
        orm_mode = True