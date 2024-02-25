from sqlalchemy.orm import Session

from schemas.pet_breed import PetBreedCreate
from db.models.pet_breed import PetBreed


def create_new_pet_breed(pet_breed: PetBreedCreate, db: Session):
    pet_breed = PetBreed(**pet_breed.dict())
    db.add(pet_breed)
    db.commit()
    db.refresh(pet_breed)
    return pet_breed