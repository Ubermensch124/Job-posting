from datetime import datetime, timedelta
from typing import Optional

from core.config import settings
from jose import jwt


def create_access_token(username: str, expire: Optional[timedelta] = None):
    if expire:
        expire_date = datetime.utcnow() + expire
    else:
        expire_date = datetime.utcnow() + timedelta(minutes=settings.JWT_TOKEN_EXPIRE)

    to_encode = {"sub": username, "exp": expire_date}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt
