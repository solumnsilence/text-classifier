import os
from pathlib import Path

from pydantic_settings import BaseSettings as PydanticBaseSettings

BASE_PATH = Path(os.path.dirname(os.path.dirname(__file__)))

STAGE = os.getenv('STAGE', 'dev')


class Settings(PydanticBaseSettings):
    """Base class for our settings from which they should be inherited.

    It is needed to simplify process of adding new settings and structure them."""

    class Config:
        case_sensitive = False
        env_file = f'{BASE_PATH}/.env.{STAGE}'
