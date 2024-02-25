from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.pet_media import PetMedia
from db.session import get_db
from db.repository.pet_media import create_new_pet_media

router = APIRouter()


@router.post("/pet-media/create-pet-media/")
def create_pet_media(pet_media : PetMedia ,db: Session = Depends(get_db)):
    pet_media = create_new_pet_media(pet_media=pet_media,db=db)
    return pet_media
