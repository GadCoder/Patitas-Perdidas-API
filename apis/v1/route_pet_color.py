from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.pet_color import PetColorCreate
from db.session import get_db
from db.repository.pet_color import create_new_pet_color

router = APIRouter()


@router.post("/pet-color/create-pet-color/")
def create_pet_color(pet_color: PetColorCreate, db: Session = Depends(get_db)):
    pet_color = create_new_pet_color(pet_color=pet_color,db=db)
    return pet_color
