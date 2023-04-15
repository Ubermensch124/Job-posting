from db.repository.users import create_new_user, get_user
from db.session import get_session
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.user_schema import UserCreateSchema, UserShowSchema
from sqlalchemy.orm import Session

users_router = APIRouter()


@users_router.post("/create", response_model=UserShowSchema)
def create_user(user: UserCreateSchema, session: Session = Depends(get_session)):
    exist_user = get_user(user.username, session)
    if exist_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Already exist")
    user = create_new_user(user=user, session=session)
    return user
