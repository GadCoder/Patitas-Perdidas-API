from sqlalchemy.orm import Session

from schemas.pet_type import PetTypeBase
from db.models.pet_type import PetType

def create_new_pet_type(pet_type: PetType, db: Session):
    pet_type = PetType(**pet_type.dict())
    db.add(pet_type)
    db.commit()
    db.refresh(pet_type)
    return pet_type