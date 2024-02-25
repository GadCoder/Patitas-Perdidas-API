from fastapi import FastAPI
from db.session import engine 
from db.base import Base     

from apis.base import api_router    

###

def include_router(app):   
	app.include_router(api_router)
      
def create_tables():         
	Base.metadata.create_all(bind=engine)
        

def start_application():
    app = FastAPI()
    create_tables()
    include_router(app)
    return app


app = start_application()


@app.get("/")
def home():
    return {"msg":"Hello FastAPI🚀"}


