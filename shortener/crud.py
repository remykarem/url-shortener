from sqlalchemy.orm import Session  # for typing
from . import models
from . import schemas


def get_urls(db: Session):
    return db.query(models.Url).all()


def create_url(db: Session, url: schemas.Url):
    hsh = hash(url.link)
    url = models.Url(link=url.link, short=hsh)
    db.add(url)
    db.commit()
    db.refresh(url)
    return url

def get_url(db: Session, short: str):
    url: str = db.query(models.Url).filter(models.Url.short == short).first()
    return url