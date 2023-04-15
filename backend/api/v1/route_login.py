from datetime import datetime

from core.config import settings
from core.hashing import Hasher
from core.security import create_access_token
from db.repository.users import get_user
from db.session import get_session
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from schemas.token_schema import Token
from sqlalchemy.orm import Session

login_router = APIRouter()


def validate_user(username: str, password: str, session: Session):
    user = get_user(username, session)
    if not user:
        return False
    if not Hasher.check_pass_hash(password, user.hashed_password):
        return False
    return user


@login_router.post("/login", response_model=Token)
def user_login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = validate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad username or password")
    access_token = create_access_token(user.username)
    return {"access_token": access_token, "token_type": "bearer"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http:localhost:80/user/login", scheme_name="JWT")


def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="bad credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        username = payload.get("sub", None)
        if payload["sub"] is None:
            raise credentials_exception
    except JWTError as exc:
        raise credentials_exception from exc
    user = get_user(username, session)
    if not user:
        raise credentials_exception
    return user
