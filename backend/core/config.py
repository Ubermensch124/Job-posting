import os

from pydantic import BaseSettings, PostgresDsn
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastApi Job Posting website"
    PROJECT_VERSION: str = "1.0.0"

    DEVELOPMENT_MODE: str = os.getenv(key="DEVELOPMENT_MODE", default="Test")

    POSTGRES_USER_TEST: str = os.getenv(key="POSTGRES_USER_TEST")
    POSTGRES_PASSWORD_TEST: str = os.getenv(key="POSTGRES_PASSWORD_TEST")
    POSTGRES_HOST_TEST: str = os.getenv(key="POSTGRES_HOST_TEST", default="localhost")
    POSTGRES_PORT_TEST: str = os.getenv(key="POSTGRES_PORT_TEST", default="5432")
    POSTGRES_DB_TEST: str = os.getenv(key="POSTGRES_DB_TEST")
    
    POSTGRES_URL_TEST: PostgresDsn = f"postgresql+psycopg2://{POSTGRES_USER_TEST}:{POSTGRES_PASSWORD_TEST}@{POSTGRES_HOST_TEST}:{POSTGRES_PORT_TEST}/{POSTGRES_DB_TEST}"

    POSTGRES_USER_PROD: str = os.getenv(key="POSTGRES_USER_PROD")
    POSTGRES_PASSWORD_PROD: str = os.getenv(key="POSTGRES_PASSWORD_PROD")
    POSTGRES_HOST_PROD: str = os.getenv(key="POSTGRES_HOST_PROD", default="localhost")
    POSTGRES_PORT_PROD: str = os.getenv(key="POSTGRES_PORT_PROD", default="5432")
    POSTGRES_DB_PROD: str = os.getenv(key="POSTGRES_DB_PROD")
    
    POSTGRES_URL_PROD: PostgresDsn = f"postgresql+psycopg2://{POSTGRES_USER_PROD}:{POSTGRES_PASSWORD_PROD}@{POSTGRES_HOST_PROD}:{POSTGRES_PORT_PROD}/{POSTGRES_DB_PROD}"

    JWT_TOKEN_EXPIRE: int = os.getenv(key="JWT_TOKEN_EXPIRE", default=30)   # minutes
    SECRET_KEY: str = os.getenv(key="SECRET_KEY")
    ALGORITHM: str = os.getenv(key="ALGORITHM", default="HS256")
    

settings = Settings()
