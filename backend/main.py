from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.routers import main_router
from core.config import settings
from db.session import session
from db.models.user import Job


def include_routers(app: FastAPI) -> None:
    app.include_router(main_router)


def staticfiles(app: FastAPI) -> None:
    app.mount('/static', StaticFiles(directory='static'), name='static')


def create_tables() -> None:
    pass
    # job = Job(title = '123123Column(String, nullable=False)',
    # company = 'Column(String, nullable=False)',
    # location = 'Column(String, nullable=False)',
    # description = 'Column(String, nullable=False)')
    
    # session.add(job)
    # session.commit()
    # session.refresh(job)


def start_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_routers(app)
    staticfiles(app)
    create_tables()
    return app


app = start_app()
print('All is good')
