# FinOS - AI-Driven Financial Orchestrator
# Copyright (C) 2026 [Your Name]
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

import numpy as np
import yfinance as yf
from sklearn.linear_model import LinearRegression


class QuantAgent:

    def calculate_6month_projection(self, symbol):
        print(f"--- Quant Agent: Calculating 180-day trend for {symbol} ---")

        df = yf.download(symbol, period="1y", interval="1d", progress=False)

        if df.empty:
            return 0, 0

        df["Day_Index"] = np.arange(len(df))
        x = df[["Day_Index"]].values
        y = df["Close"].values

        model = LinearRegression()
        model.fit(x, y)

        future_day = np.array([[len(df) + 180]])
        projected_price = float(model.predict(future_day)[0][0])

        current_price = float(y[-1][0])
        pct_change = ((projected_price - current_price) / current_price) * 100

        return round(projected_price, 2), round(pct_change, 2)
