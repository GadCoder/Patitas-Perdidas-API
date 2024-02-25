from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.pet_type import PetTypeBase
from db.session import get_db
from db.repository.pet_type import create_new_pet_type

router = APIRouter()


@router.post("/pet-type/create-pet-type/")
def create_pet_type(pet_type : PetTypeBase ,db: Session = Depends(get_db)):
    pet_type = create_new_pet_type(pet_type=pet_type,db=db)
    return pet_type
