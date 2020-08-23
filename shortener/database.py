from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    "postgresql+psycopg2://raimi:mysecretpassword@localhost/postgres")

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
