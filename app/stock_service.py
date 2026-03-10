from __future__ import annotations

from sqlmodel import SQLModel

from .marketstack_client import MarketstackClient, MarketstackNotFoundError, MarketstackError
from .models import StockEODData


class StockService:
    def __init__(self, client: MarketstackClient | None = None) -> None:
        self.client = client or MarketstackClient()

    async def get_eod_for_symbol(self, symbol: str) -> StockEODData:
        normalized = symbol.strip().upper()
        if not normalized:
            raise ValueError("Ticker symbol must not be empty.")

        try:
            eod_raw = await self.client.get_eod(normalized)
        except MarketstackNotFoundError:
            raise
        except MarketstackError:
            raise

        # Map Marketstack payload to StockEODData model
        # Marketstack fields: symbol, date, open, high, low, close, volume, etc.
        return StockEODData(
            symbol=eod_raw.get("symbol", normalized),
            date=eod_raw["date"],
            open=eod_raw["open"],
            high=eod_raw["high"],
            low=eod_raw["low"],
            close=eod_raw["close"],
            volume=eod_raw.get("volume"),
        )

