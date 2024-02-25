from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.pet_breed import PetBreed
from db.session import get_db
from db.repository.pet_breed import create_new_pet_breed

router = APIRouter()


@router.post("/pet-breed/create-pet-breed/")
def create_pet_breed(pet_breed : PetBreed ,db: Session = Depends(get_db)):
    pet_breed = create_new_pet_breed(pet_breed=pet_breed,db=db)
    return pet_breed
