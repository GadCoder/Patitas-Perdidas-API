from pydantic import BaseModel


class PetBreedBase(BaseModel):
    name: str
    breed_name: str
    pet_type_id: int


class PetBreed(PetBreedBase):
    id: int

    class Config:
        orm_mode = True