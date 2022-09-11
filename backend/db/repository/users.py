from schemas.user_schema import UserCreateSchema
from sqlalchemy.orm import Session
from db.models.user import User
from core.hashing import Hasher


def create_new_user(user: UserCreateSchema, db: Session):
    user = User(username=user.username,
        email = user.email,
        hashed_password=Hasher.get_hash_from_pass(password=user.password),
        is_active=True,
        is_superuser=False
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user    