from typing import Optional
from pydantic import BaseModel


class Url(BaseModel):
    link: str
    short: Optional[str]
