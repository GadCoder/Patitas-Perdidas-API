from fastapi import APIRouter

from apis.v1 import (route_user,
                     route_pet_breed,
                     route_pet_color,
                     route_pet_media,
                     route_pet_status,
                     route_pet_type,
                     route_pet,
                     route_login,
                     route_html)

api_router = APIRouter()
api_router.include_router(route_user.router,prefix="",tags=["users"])
api_router.include_router(route_pet_breed.router,prefix="",tags=["pet_breeds"])
api_router.include_router(route_pet_color.router,prefix="",tags=["pet_colors"]) 
api_router.include_router(route_pet_media.router,prefix="",tags=["pet_media"])
api_router.include_router(route_pet_status.router,prefix="",tags=["pet_status"])
api_router.include_router(route_pet_type.router,prefix="",tags=["pet_type"])
api_router.include_router(route_pet.router,prefix="",tags=["pets"])
api_router.include_router(route_login.router, prefix="", tags=["login"])
api_router.include_router(route_html.router, prefix="", tags=["html"])
