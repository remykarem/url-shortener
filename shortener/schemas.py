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
    url_hash = str(abs(url_hash))[:9]
    url_short = f"{url_hash[:3]}-{url_hash[3:6]}-{url_hash[6:9]}"
    return url_hash, url_short
