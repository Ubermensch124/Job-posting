from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os, sys
import sqlalchemy

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from core.config import settings
from models.user import User
from models.user import Job
from models.user import Base


def create_session(mode: str = 'Test'):
    if mode.lower() == 'test':
        DATABASE_URL = settings.POSTGRES_URL_TEST
    else:
        DATABASE_URL = settings.POSTGRES_URL_PROD

    engine = create_engine(url=DATABASE_URL)
    session = Session(bind=engine)

    if mode.lower() == 'test':
        if sqlalchemy.inspect(engine).has_table("job"):
            Job.__table__.drop(engine)
        if sqlalchemy.inspect(engine).has_table("users"):
            User.__table__.drop(engine)

    Base.metadata.create_all(bind=engine)

    return session       


session = create_session(mode=settings.DEVELOPMENT_MODE)
