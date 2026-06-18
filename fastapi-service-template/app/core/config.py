from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "example-fastapi-service"
    app_version: str = "0.1.0"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    log_level: str = "INFO"
    openapi_public_prefixes: list[str] = Field(default_factory=lambda: ["/health", "/metrics", "/docs", "/openapi.json"])


settings = Settings()
