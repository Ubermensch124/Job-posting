from schemas.user_schema import UserCreateSchema
from sqlalchemy.orm import Session
from db.models.user import User
from core.hashing import Hasher


def create_new_user(user: UserCreateSchema, session: Session):
    user = User(
        username=user.username,
        email = user.email,
        hashed_password=Hasher.get_hash_from_pass(password=user.password),
        )
    session.add(user)
    session.commit()
    session.refresh(user)
    
    return user


def get_user(username: str, session: Session):
    user = session.query(User).filter(User.username == username).first()
    if not user:
        return None
    return user
