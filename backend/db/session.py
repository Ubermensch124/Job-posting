import os
import sys
from typing import Generator

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, declarative_base

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from core.config import settings
# from models.user import Base, Job, User

# def create_session(mode: str = 'Test'):
#     if mode.lower() == 'test':
#         DATABASE_URL = settings.POSTGRES_URL_TEST
#     else:
#         DATABASE_URL = settings.POSTGRES_URL_PROD

#     engine = create_engine(url=DATABASE_URL)
#     SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#     if mode.lower() == 'test':
#         if sqlalchemy.inspect(engine).has_table("job"):
#             Job.__table__.drop(engine)
#         if sqlalchemy.inspect(engine).has_table("users"):
#             User.__table__.drop(engine)

#     Base.metadata.create_all(bind=engine)

#     return session


# session = create_session(mode=settings.DEVELOPMENT_MODE)

engine = create_engine(url=settings.POSTGRES_URL_PROD)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# Base.metadata.create_all(bind=engine)

def get_session() -> Generator:
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()
