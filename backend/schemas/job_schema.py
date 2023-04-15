from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JobCreateSchema(BaseModel):
    title: str
    company: str
    company_url: Optional[str] = None
    location: str
    description: str
    data_posted: Optional[datetime]
    is_active: Optional[bool] = True


class JobShowSchema(BaseModel):
    title: str
    company: str
    description: str

    class Config:  # non dict obj to json
        orm_mode = True
