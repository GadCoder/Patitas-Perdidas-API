from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db.session import engine 
from db.base import Base     

from apis.base import api_router    



def include_router(app):   
	app.include_router(api_router)
      
def create_tables():         
	Base.metadata.create_all(bind=engine)
        

def start_application():
    app = FastAPI()
    create_tables()
    include_router(app)
    return app

templates = Jinja2Templates(directory="templates")

app = start_application()


@app.get("/login-page/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
          request=request, name="index.html", context={}
    )

