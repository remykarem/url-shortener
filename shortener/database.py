import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(os.environ["DATABASE_URL"])

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
