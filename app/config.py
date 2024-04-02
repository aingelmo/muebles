from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    env: str = Field(default=None)
    credentials: str = Field(default="firebaseapp/credentials.json")

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


ROOT_DIR = Path(__file__).parents[1]

settings = Settings()
ENV = settings.env
CREDENTIALS = settings.credentials
