from sqlalchemy.orm import Session

from schemas.pet_breed import PetBreed
from db.models.pet_breed import PetBreed

def create_new_pet_breed(pet_breed: PetBreed, db: Session):
    pet_breed = PetBreed(**pet_breed.dict())
    db.add(pet_breed)
    db.commit()
    db.refresh(pet_breed)
    return pet_breed