from __future__ import annotations

from typing import Any, Dict, List

import httpx

from .settings import get_settings


class MarketstackError(Exception):
    """Base exception for Marketstack-related errors."""


class MarketstackNotFoundError(MarketstackError):
    """Raised when no EOD data is found for the given symbol."""


class MarketstackClient:
    def __init__(self, api_key: str | None = None, base_url: str | None = None) -> None:
        settings = get_settings()
        self.api_key = api_key or settings.marketstack_api_key
        self.base_url = (base_url or settings.marketstack_base_url).rstrip("/")

    async def get_eod(self, symbol: str) -> Dict[str, Any]:
        """Return the latest EOD data for a ticker or raise a domain-specific error."""
        url = f"{self.base_url}/eod"
        params = {
            "access_key": self.api_key,
            "symbols": symbol,
            "limit": 1,
        }

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(url, params=params)
        except httpx.HTTPError as exc:
            raise MarketstackError(f"Network error calling Marketstack: {exc}") from exc

        if response.status_code >= 500:
            raise MarketstackError(
                f"Marketstack service error (status {response.status_code})"
            )

        data = response.json()

        if "error" in data:
            message = data["error"].get("message", "Unknown Marketstack error")
            raise MarketstackError(message)

        entries: List[Dict[str, Any]] = data.get("data") or []
        if not entries:
            raise MarketstackNotFoundError(
                f"No EOD data found for symbol '{symbol}'."
            )

        # Return the first (most recent) entry
        return entries[0]

