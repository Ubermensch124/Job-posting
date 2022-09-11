import datetime
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# from base_class import Base
# 
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    # jobs = relationship('Job', back_populates='owner')


class Job(Base):
    __tablename__ = 'job'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    company_url = Column(String)
    location = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date_posted = Column(Date, default=datetime.date.today())
    is_active = Column(Boolean, default=True)

    # owner_id = Column(Integer, ForeignKey('users.id'))
    # owner = relationship('User', back_populates = 'jobs')
