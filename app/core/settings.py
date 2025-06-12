# app/core/settings.py
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    contact_email: str = Field(..., env="CONTACT_EMAIL")
    osm_api_base: str = Field(..., env="OSM_API_BASE")
    log_level: str = "INFO"
    feeds_config_path: str = "config/feeds.json"

    class Config:
        env_file = ".env"

settings = Settings()