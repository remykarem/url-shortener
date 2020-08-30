from sqlalchemy.orm import Session  # for typing
from . import models
from . import schemas


def get_urls(db: Session) -> [schemas.UrlRead]:
    return db.query(models.Url).all()


def create_short(db: Session, url: schemas.UrlCreate) -> schemas.UrlShort:
    url_hsh, url_short = schemas.hasher(url.raw)
    url = models.Url(raw=url.raw, hsh=url_hsh)
    db.add(url)
    db.commit()
    db.refresh(url)
    return url_short


def get_url(db: Session, hsh: str) -> str:
    url = db.query(models.Url).filter(models.Url.hsh == hsh).first()
    return url
