from sqlalchemy.orm import Session
from schemas.pet_color import PetColorCreate
from db.models.pet_color import PetColor


def create_new_pet_color(pet_color: PetColorCreate, db: Session):
    pet_color = PetColor(**pet_color.dict())
    db.add(pet_color)
    db.commit()
    db.refresh(pet_color)
    return pet_color


def retrieve_all_pets_colors(db: Session):
    pets_colors = db.query(PetColor).all()
    return pets_colors
