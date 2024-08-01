from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: str
    bot_admins: list[int] = Field(default_factory=list)

    model_config = SettingsConfigDict(env_ignore_empty=True)


settings = Settings(_env_file=(".env.example", ".env"))
