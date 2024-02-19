from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import Settings

engine = create_engine(Settings().DATABASE_URL)
Base = declarative_base()
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    try:
        db = session()
        yield db
    finally:
        db.close()
