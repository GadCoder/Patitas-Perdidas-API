from datetime import datetime
from datetime import date

from fastapi.responses import HTMLResponse
from fastapi import Depends, APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from apis.v1.route_login import authenticate_user

from core.config import settings
from db.repository.pet_media import retrieve_all_pet_media
from db.session import get_db
from db.repository.pet import create_new_pet, retrieve_all_pets
from db.repository.pet_breed import retrieve_breeds_from_pet_type
from db.repository.pet_color import retrieve_all_pets_colors
from db.repository.pet_type import retrieve_pets_type
from typing import Annotated

from fastapi import FastAPI, File, UploadFile
import boto3

from typing import Annotated

from botocore.exceptions import NoCredentialsError

from schemas.pet import PetCreate


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/login-page/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
          request=request, name="index.html", context={}
    )



@router.get("/register-page/", response_class=HTMLResponse)
async def register_pet_page(request: Request, db: Session= Depends(get_db)):
    pets_type = retrieve_pets_type(db=db)
    pet_colors = retrieve_all_pets_colors(db=db)
    pet_breeds = retrieve_breeds_from_pet_type(pet_type_id=1, db=db)
    return templates.TemplateResponse(
          request=request, name="register.html", context={
              "pet_types": pets_type,
              "pet_colors": pet_colors,
              "pet_breeds": pet_breeds
          }
    )


@router.post("/register-pet/", response_class=HTMLResponse)
async def register_pet(request: Request,
                        name: Annotated[str, Form()],
                        district: Annotated[str, Form()],
                        raza: Annotated[int, Form()],
                        tipo_mascota: Annotated[int, Form()],
                        color: Annotated[int, Form()],
                        db: Session= Depends(get_db),
                        files: list = File(...),
                        ):
    pet = PetCreate(
        name=name,
        district=district,
        report_date=date.today(),
        breed_id=raza,
        status_id=1,
        pet_type_id=tipo_mascota,
        pet_color_id=color,
        user_id=1
    )
    pet_on_db = create_new_pet(pet=pet, db=db)
    if pet_on_db is None:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error al registrar la mascota"
        )

    return templates.TemplateResponse(
          request=request, name="register-completed.html", context={}
    )

    for file in files:
        upload_to_aws(file, pet_id = pet.id)


@router.get("/home-page/", response_class=HTMLResponse)
async def login(request: Request,  db: Session= Depends(get_db)):
    user = authenticate_user("barbas@gmail.com", "barbas", db=db)
    if not user:
          return templates.TemplateResponse(
                request=request, name="login-error.html", context={
                    "user": user
                }
            )

    pets = retrieve_all_pets(db)
    pets_type = retrieve_pets_type(db=db)
    pet_colors = retrieve_all_pets_colors(db=db)
    pet_media = retrieve_all_pet_media(db=db)

    return templates.TemplateResponse(
                request=request, name="homepage.html", context={
                    "user": user.names,
                    "pets": pets,
                    "pets_colors": pet_colors,
                    "pet_media": pet_media,
                }
            )