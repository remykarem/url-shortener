from sqlalchemy import Column, Integer, String
from .database import Base


class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    raw = Column(String)
    hsh = Column(String)

    def __repr__(self):
        return f"Url(raw='{self.raw}', hsh='{self.hsh}')"
