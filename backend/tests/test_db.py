import os, sys

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 

from schemas.user_schema import UserCreateSchema
from db.repository.users import create_new_user
from db.models.user import User
from core.config import settings
from db.models.user import Base


def test_user_schema():
    user = UserCreateSchema(username='Ubermensch124', email='mark.k.2012@yandex.ru', password='123qwerty')
    assert (user.username, user.email, user.password) == ('Ubermensch124', 'mark.k.2012@yandex.ru', '123qwerty')


def test_user_show_schema():
    user = UserCreateSchema(username='123', email='mark.k.2012@yandex.ru', password='123qwerty')

    engine = create_engine(url=settings.POSTGRES_URL_TEST)
    session = Session(bind=engine)
    User.__table__.drop(engine)
    Base.metadata.create_all(bind=engine)
    ans = create_new_user(user=user, db=session)

    assert session.query(User).first().username == user.username
