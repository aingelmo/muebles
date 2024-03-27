from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresSettings(BaseSettings):
    user: str = Field(validation_alias="POSTGRES_USER")
    password: str = Field(validation_alias="POSTGRES_PASSWORD")
    host: str = Field(validation_alias="POSTGRES_HOST")
    db_name: str = Field(validation_alias="POSTGRES_DB")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
