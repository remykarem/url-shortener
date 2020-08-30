from typing import List

from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session  # for typing

from .database import engine, SessionLocal
from .models import Base
from . import schemas
from . import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/public", StaticFiles(directory="public"), name="public")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return FileResponse("public/index.html")


@app.get("/urls/", response_model=List[schemas.UrlRead])
def read_urls(db: Session = Depends(get_db)):
    """For debugging"""
    urls = crud.get_urls(db)
    return urls


@app.post("/urls/")
def create_url(url: schemas.UrlCreate, db: Session = Depends(get_db)):
    crud.create_url(db=db, url=url)
    return {"status": 1}


@app.get("/{short}", response_model=schemas.UrlRead)
def get_url(short: str, db: Session = Depends(get_db)):
    url = crud.get_url(db=db, short=short)
    return RedirectResponse(url=f"http://{url.link}")
