from typing import NewType, Tuple
from pydantic import BaseModel

UrlRaw = NewType("UrlRaw", str)  # google.com
UrlHash = NewType("UrlHash", str)  # 542565888
UrlShort = NewType("UrlShort", str)  # 542-565-888
UrlShortLink = NewType("UrlShortLink", str)  # <appname>/542-565-888

NUM_DIGITS = 9
GROUPS = 3


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
    url_short = hash_to_short(url_hash)
    return url_hash, url_short


def hash_to_short(url_hash: UrlHash) -> UrlShort:
    arr = [url_hash[i*GROUPS:(i+1)*GROUPS]
           for i in range(GROUPS)]
    return "-".join(arr)
