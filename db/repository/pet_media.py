from sqlalchemy.orm import Session

from schemas.pet_media import PetMedia
from db.models.pet_media import PetMedia

def create_new_pet_media(pet_media: PetMedia, db: Session):
    pet_media = PetMedia(**pet_media.dict())
    db.add(pet_media)
    db.commit()
    db.refresh(pet_media)
    return pet_media