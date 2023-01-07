from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base
# import os
# from dotenv import load_dotenv

# load_dotenv()

# database_url = os.getenv("DATABASE_URL")

engine = create_engine("postgresql://postgres:local1postgres1@192.168.29.128:5444/authentication")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
