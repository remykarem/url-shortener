from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session  # for typing

from .database import engine, SessionLocal
from .models import Base
from . import schemas
from . import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return {"Hello": "World"}


@app.get("/urls/")
def read_urls(db: Session = Depends(get_db)):
    urls = crud.get_urls(db)
    return urls


@app.post("/urls/")
def create_url(url: schemas.Url, db: Session = Depends(get_db)):
    return crud.create_url(db=db, url=url)


@app.get("/{short}")
def get_url(short: str, db: Session = Depends(get_db)):
    return crud.get_url(db=db, short=short)