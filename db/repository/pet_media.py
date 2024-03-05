from sqlalchemy.orm import Session

from schemas.pet_media import PetMediaBase
from db.models.pet_media import PetMedia

def create_new_pet_media(pet_media: PetMediaBase, db: Session):
    pet_media = PetMedia(**pet_media.dict())
    db.add(pet_media)
    db.commit()
    db.refresh(pet_media)
    return pet_media


def retrieve_all_pet_media(db: Session):
    pet_media = db.query(PetMedia).all()
    return pet_media