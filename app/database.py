from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#sqlite database url - creates file "vibeckeck.db"
SQLALCHEMY_DATABASE_URL = "sqlite:///./vibecheck.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} #needed to work with fastapi
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)#factory for databse sessions
Base = declarative_base()#creates base class for tables

def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()