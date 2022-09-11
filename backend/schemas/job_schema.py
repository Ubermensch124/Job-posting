from typing import Optional
from pydantic import BaseModel


class JobCreateSchema(BaseModel):
    title: str 
    company: str
    location: str
    description: str


class JobShowSchema(BaseModel):
    title: str 
    company: str
    is_active: bool

    class Config():   # non dict obj to json
        orm_mode = True
