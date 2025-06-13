import os
from pathlib import Path
from typing import Set
from urllib.parse import quote_plus

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings:
    DEBUG: bool = True
    SERVICE_PORT: int = int(os.getenv("SERVICE_PORT", 8002))
    BASE_DIR: str = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    TEMP_DIRECTORY: Path = Path("/tmp/")
    MAX_CONTENT_LENGTH: int = 16 * 1024 * 1024  # 16MB

    # File extension settings
    IMAGE_ALLOWED_EXTENSIONS: Set[str] = {
        "jpeg", "pgm", "webp", "bmp", "JPEG", "JPG", "jpg", "png", "ppm"
    }
    VIDEO_ALLOWED_EXTENSIONS: Set[str] = {
        "3gp", "mp4", "avi", "mov", "mkv", "wmv", "flv", "webm"
    }
    DOCUMENT_ALLOWED_EXTENSIONS: Set[str] = {"pdf"}

    # PostgreSQL Database Configuration
    DATABASE_HOST: str = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT: int = int(os.getenv("DATABASE_PORT", 5432))
    DATABASE_USER: str = os.getenv("DATABASE_USER", "postgres")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "ksar0805")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "mydatabase")
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    )

    # Secret key for validation
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default_secret_key")

    # Encoding the password for use in URL
    DATABASE_PASSWORD_ENCODED: str = quote_plus(DATABASE_PASSWORD)

    # Async Database URL with the encoded password
    ASYNC_DATABASE_URL: str = (
        f"postgresql+asyncpg://{DATABASE_USER}:{DATABASE_PASSWORD_ENCODED}@"
        f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    )

    # Allowed origins for CORS
    ALLOW_ORIGINS: Set[str] = set(os.getenv("ALLOW_ORIGINS", "*").split(","))

    # Frontend URL
    FRONTEND_URL: str = os.getenv("FRONTEND_URL", "http://localhost:3000")