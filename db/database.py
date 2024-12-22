from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg2://postgres:password@localhost:5432/game_db"

# SQLAlchemy Base
Base = declarative_base()

# Engine and Session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
