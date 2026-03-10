from __future__ import annotations

import os
from functools import lru_cache

from dotenv import load_dotenv

# Load environment variables from a .env file at project root, if present
load_dotenv()


class Settings:
    """Application settings loaded from environment variables."""

    marketstack_base_url: str = "http://api.marketstack.com/v2"
    marketstack_api_key: str

    def __init__(self) -> None:
        api_key = os.getenv("MARKETSTACK_ACCESS_KEY")
        if not api_key:
            raise RuntimeError(
                "MARKETSTACK_ACCESS_KEY environment variable is not set. "
                "Set it to your Marketstack API access key."
            )
        self.marketstack_api_key = api_key


@lru_cache
def get_settings() -> Settings:
    return Settings()

