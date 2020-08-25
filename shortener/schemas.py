from typing import Optional
from pydantic import BaseModel


class UrlBase(BaseModel):
    link: str
    short: str


class UrlRead(UrlBase):
    id: int

    class Config:
        orm_mode = True
