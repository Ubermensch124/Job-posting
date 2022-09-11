import os
from dotenv import load_dotenv
from pathlib import Path


# env_path = Path('.') / '.env'
env_path = 'C:/Users/Mark/Desktop/English study website/backend/.env'
# env_path = '../.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME: str = "FastApi English study website"
    PROJECT_VERSION: str = "1.0.0"

    DEVELOPMENT_MODE: str = os.getenv(key='DEVELOPMENT_MODE', default='Test')

    POSTGRES_USER_TEST: str = os.getenv(key="POSTGRES_USER_TEST")
    POSTGRES_PASSWORD_TEST: str = os.getenv(key="POSTGRES_PASSWORD_TEST")
    POSTGRES_HOST_TEST: str = os.getenv(key="POSTGRES_HOST_TEST", default='localhost')
    POSTGRES_PORT_TEST: str = os.getenv(key="POSTGRES_PORT_TEST", default=5432)
    POSTGRES_DB_TEST: str = os.getenv(key="POSTGRES_DB_TEST")
    POSTGRES_URL_TEST: str = f"postgresql+psycopg2://{POSTGRES_USER_TEST}:{POSTGRES_PASSWORD_TEST}@{POSTGRES_HOST_TEST}:{POSTGRES_PORT_TEST}/{POSTGRES_DB_TEST}"

    POSTGRES_USER_PROD: str = os.getenv(key="POSTGRES_USER_PROD")
    POSTGRES_PASSWORD_PROD: str = os.getenv(key="POSTGRES_PASSWORD_PROD")
    POSTGRES_HOST_PROD: str = os.getenv(key="POSTGRES_HOST_PROD", default='localhost')
    POSTGRES_PORT_PROD: str = os.getenv(key="POSTGRES_PORT_PROD", default=5432)
    POSTGRES_DB_PROD: str = os.getenv(key="POSTGRES_DB_PROD")
    POSTGRES_URL_PROD: str = f"postgresql+psycopg2://{POSTGRES_USER_PROD}:{POSTGRES_PASSWORD_PROD}@{POSTGRES_HOST_PROD}:{POSTGRES_PORT_PROD}/{POSTGRES_DB_PROD}"


settings = Settings()
