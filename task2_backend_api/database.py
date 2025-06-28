from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings

DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@localhost/{settings.database_name}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
