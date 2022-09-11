from fastapi import APIRouter
from sqlalchemy.orm import Session

from db.repository.users import create_new_user
from db.session import session
from schemas.user_schema import UserCreateSchema, UserShowSchema


users_router = APIRouter()

@users_router.post('', response_model=UserShowSchema)
def create_user(user: UserCreateSchema):
    user = create_new_user(user=user, db=session)
    return user
