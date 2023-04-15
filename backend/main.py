import uvicorn
from api.routers import main_router
from core.config import settings
from db.session import Base, engine
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


def include_routers(application: FastAPI) -> None:
    application.include_router(main_router)


def staticfiles(application: FastAPI) -> None:
    application.mount("/static", StaticFiles(directory="static"), name="static")


def start_app() -> FastAPI:
    application = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_routers(application)
    staticfiles(application)
    return application


app = start_app()


@app.on_event("startup")
def db():
    Base.metadata.create_all(engine)


# @app.on_event("shutdown")
# def db():
#     Base.metadata.drop_all(engine)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=80, reload=True)
