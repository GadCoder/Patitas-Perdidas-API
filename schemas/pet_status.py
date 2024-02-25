from pydantic import BaseModel


class PetStatusBase(BaseModel):
    name: str
    status: str


class PetStatusCreate(PetStatusBase):
    pass


class PetStatus(PetStatusBase):
    id: int

    class Config:
        orm_mode = True