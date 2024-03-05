from pydantic import BaseModel


class PetBreedBase(BaseModel):
    breed: str
    pet_type_id: int


class PetBreedCreate(PetBreedBase):
    pass


class PetBreed(PetBreedBase):
    id: int

    class Config:
        orm_mode = True