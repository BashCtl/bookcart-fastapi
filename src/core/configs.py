from pydantic_settings import BaseSettings
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

    class ConfigDict:
        env_file = '.env'

settings = Settings()
