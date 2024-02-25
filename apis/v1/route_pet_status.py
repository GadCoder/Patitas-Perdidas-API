from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.pet_status import PetStatus
from db.session import get_db
from db.repository.pet_status import create_new_pet_status

router = APIRouter()


@router.post("/pet-status/create-pet-status/")
def create_pet_status(pet_status : PetStatus ,db: Session = Depends(get_db)):
    pet_status = create_new_pet_status(pet_status=pet_status,db=db)
    return pet_status
