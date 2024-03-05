from sqlalchemy.orm import Session

from schemas.pet import PetCreate
from db.models.pet import Pet


def create_new_pet(pet:PetCreate, db: Session):
    pet = Pet(
        name=pet.name,
        district=pet.district,
        report_date=pet.report_date,
        breed_id=pet.breed_id,
        status_id=pet.status_id,
        pet_type_id=pet.pet_type_id,
        pet_color_id=pet.pet_color_id,
        user_id=pet.user_id
    )
    db.add(pet)
    db.commit()
    db.refresh(pet)
    return pet


def retrieve_pets_from_user(user_id: int, db: Session):
    pets = db.query(Pet).filter(Pet.user_id == user_id).all()
    return pets

def retrieve_all_pets(db: Session):
    pets = db.query(Pet).all()
    return pets
    