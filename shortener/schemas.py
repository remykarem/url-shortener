from typing import NewType, Tuple
from pydantic import BaseModel

UrlRaw = NewType("UrlRaw", str)
UrlHash = NewType("UrlHash", str)
UrlShort = NewType("UrlShort", str)
UrlShortLink = NewType("UrlShortLink", str)


class UrlBase(BaseModel):
    raw: str
    short: str


class UrlRead(UrlBase):
    id: int

    class Config:
        orm_mode = True


class UrlCreate(BaseModel):
    raw: str


def hasher(url_raw: UrlRaw) -> Tuple[UrlHash, UrlShort]:
    url_hash = hash(url_raw)
    url_hash = str(abs(url_hash))[:12]
    url_short = f"{url_hash[:4]}-{url_hash[4:8]}-{url_hash[8:12]}"
    return url_hash, url_short
