from fastapi.responses import HTMLResponse
from fastapi import Depends, APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi import status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from core.config import settings
from db.session import get_db
from core.security import create_access_token
from db.repository.pet import create_new_pet, retrieve_all_pets
from db.repository.pet_breed import retrieve_breeds_from_pet_type
from db.repository.pet_color import retrieve_all_pets_colors
from db.repository.pet_type import retrieve_pets_type
from typing import Annotated

from fastapi import FastAPI, File, UploadFile
import boto3

from botocore.exceptions import NoCredentialsError


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
async def register_pet(request: Request, form_data: str = Form(...),  db: Session= Depends(get_db), files: list = File(...),):
    pet = create_new_pet(
        name=form_data.name,
        district=form_data.district,
        report_date=form_data.date,
        breed_id=form_data.breed_id,
        status_id=1,
        pet_type_id=form_data.pet_type_id,
        pet_color_id=form_data.pet_color_id,
        user_id=1
    )
    
    return templates.TemplateResponse(
          request=request, name="succesful-register.html", context={}
    )

    for file in files:
        upload_to_aws(file, pet_id = pet.id)

