import logging
import sys
from typing import List
import os

from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

from .logg import InterceptHandler

API_PREFIX = "/api"

JWT_TOKEN_PREFIX = "Token"  # noqa: S105
VERSION = "0.0.0"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES= 5
config = Config(".env", os.environ)

DEBUG: bool = config("DEBUG", cast=bool, default=False)

DATABASE_URL: str = config("DB_CONNECTION", cast=str, default='')
DATABASE_NAME: str = config("DB_NAME", cast=str)
MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)

SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret, default="This is a secret key for development")

PROJECT_NAME: str = config("PROJECT_NAME", default="Radio Tefa")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)

# DB Collections Names
category_collection_name = "Category"
# logging configuration

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")

logging.getLogger().handlers = [InterceptHandler()]
for logger_name in LOGGERS:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]

logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
