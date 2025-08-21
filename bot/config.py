from pydantic_settings import BaseSettings
from pydantic import Field
from pathlib import Path


class Settings(BaseSettings):
    POSTGRES_USER: str = Field(description="Пользователь БД")
    POSTGRES_PASSWORD: str = Field(description="Пароль БД")
    POSTGRES_DB: str = Field(description="Название БД")
    DB_URL: str = Field(description="URL БД")
    BOT_TOKEN: str = Field(description="Секретный токен бота")

    class Config:
        env_file = Path(__file__).resolve().parents[1] / ".env"
        env_file_encoding = "utf-8"


settings = Settings()