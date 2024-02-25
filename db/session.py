import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator            

load_dotenv()

SQLALCHEMY_DATABASE_URL =  os.environ["DATABASE_URL"]

engine = create_engine(
     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db() -> Generator:   #new
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()