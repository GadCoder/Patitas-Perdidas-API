from sqlalchemy.orm import Session

from schemas.pet_status import PetStatusCreate
from db.models.pet_status import PetStatus


def create_new_pet_status(pet_status: PetStatusCreate, db: Session):
    pet_status = PetStatus(**pet_status.dict())
    db.add(pet_status)
    db.commit()
    db.refresh(pet_status)
    return pet_status


def retrieve_all_pet_status(db: Session):
    pet_status = db.query(PetStatus).all()
    return pet_status

