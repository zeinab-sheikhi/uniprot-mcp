"""Configuration settings for Uniprot MCP server."""

from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Server settings
    SERVER_NAME: str = "UniprotMCP"
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 9000
    TRANSPORT: Literal["stdio", "streamable-http"] = "streamable-http"

    # API settings
    MAX_RETIRES: int = 3
    REQUEST_TIMEOUT: int = 10

    # Cache settings
    CACHE_TTL: int = 86400  # 24 hours
    CACHE_DIR: str | None = None

    # SSL/TLS settings
    SSL_CERT_FILE: str | None = None
    SSL_KEY_FILE: str | None = None

    # Logging
    LOG_LEVEL: str = "INFO"

    # AlphaFold API settings
    ANTHROPIC_API_KEY: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow",
    )


settings = Settings()
