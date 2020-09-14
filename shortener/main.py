import os
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

HOSTNAME = os.getenv(
    "HOSTNAME", "https://whispering-hamlet-28439.herokuapp.com/")

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
def create_short_link(url: schemas.UrlCreate, db: Session = Depends(get_db)):
    short = crud.get_short(db=db, raw=url.raw)
    if short is None:
        short = crud.create_short(db=db, url=url)
    url_short_link = f"{HOSTNAME}{short}"
    return {"shortLink": url_short_link}


@app.get("/{short}", response_model=schemas.UrlRead)
def redirect(short: str, db: Session = Depends(get_db)):
    hsh = short.replace("-", "")
    url = crud.get_raw(db=db, hsh=hsh)

    if url is None:
        return FileResponse("public/404.html", status_code=404)

    return RedirectResponse(url=f"{url.raw}")
