from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.pet import PetCreate
from db.session import get_db
from db.repository.pet import create_new_pet, retrieve_pets_from_user

router = APIRouter()


@router.post("/pets/create-pet/")
def create_user(pet : PetCreate, db: Session = Depends(get_db)):
    pet = create_new_pet(pet=pet,db=db)
    return pet 

@router.get("/pets/get-pets-from-user")
def get_pets_from_user(user_id: int, db: Session = Depends(get_db)):
    pets_from_user = retrieve_pets_from_user(user_id=user_id, db=db)
    return pets_from_user

