import os.path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    CMC_API_KEY: str

    model_config = SettingsConfigDict(env_file=os.path.join(os.path.abspath(os.path.curdir), '../.env'))


settings = Settings()