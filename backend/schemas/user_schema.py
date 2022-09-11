from pydantic import BaseModel, EmailStr


class UserCreateSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserShowSchema(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

    class Config():
        orm_mode = True