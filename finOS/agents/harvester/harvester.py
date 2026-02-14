# FinOS - AI-Driven Financial Orchestrator
# Copyright (C) 2026 Eduardo Querido
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import pandas as pd
import yfinance as yf
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)


class HarvesterAgent:
    def __init__(self, api_key):
        self.ts = TimeSeries(key=api_key, output_format="pandas")
        self.ti = TechIndicators(key=api_key, output_format="pandas")

    @retry(
        wait=wait_exponential(multiplier=1, min=4, max=10),
        stop=stop_after_attempt(3),
        retry=retry_if_exception_type(ValueError),
    )
    def fetch_av_data(self, symbol):
        """Alpha Vantage cal with automatic retry rate limit"""
        data, meta_data = self.ts.get_daily(symbol=symbol, outputsize="compact")
        sma, _ = self.ti.get_sma(symbol=symbol, interval="daily", time_period=20)
        return data, sma, meta

    def fetch_fallback_data(self, symbol):
        """
        Yahoo Finance fallback.
        No rate limite, but fewer indicators
        """
        ticker = yf.Ticker(symbol)
        history = ticker.history(period="1mo")

        history["SMA"] = history["Close"].rolling(window=20).mean()
        return history["Close"].iloc[-1], history["SMA"].iloc[-1]

    def get_latest_news(self, symbol):
        """
        Fetches latest news via yfinance
        """
        ticker = yf.Ticker(symbol)
        news = ticker.news

        headlines = [article.get("content").get("title") for article in news]
        return headlines[:5]  # top 5 articles

    def get_market_vitals(self, symbol):
        """
        Fetches both Price and Sentiment
        """
        print(f"--- Harvest Agent starting scan for {symbol} ---")

        try:
            data, sma, meta = self.fetch_av_data(symbol)
            current_price = data["4. close"].iloc[
                -1
            ]  # numbered name convention from Alpha Vantage
            sma_20 = sma["SMA"].iloc[-1]
            last_updated = meta["3. Last Refreshed"]
        except Exception as e:
            current_price, sma_20 = self.fetch_fallback_data(symbol)
            last_updated = "Live (Yahoo)"

        headlines = self.get_latest_news(symbol)

        return {
            "symbol": symbol,
            "price": round(current_price, 2),
            "sma_20": round(sma_20, 2),
            "last_updated": last_updated,
            "headlines": headlines,
            "signal": "BULLISH" if current_price > sma_20 else "BEARISH",
        }
