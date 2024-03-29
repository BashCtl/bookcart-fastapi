from pydantic_settings import BaseSettings
from typing import List
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str
    DB_URI: str
    DB_NAME: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    SECRET_KEY: str
    JWT_REFRESH_SECRET: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: str
    API_VERSION: str
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    ALLOW_METHODS: List[str] = ["*"]
    ALLOW_HEADERS: List[str] = ["*"]

    class ConfigDict:
        env_file = '.env'


settings = Settings()
