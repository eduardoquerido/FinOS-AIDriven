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

import os
import sys

from dotenv import load_dotenv

from orchestration.financial_orchestrator import FinancialOrchestrator

load_dotenv()


def main():
    # check if the user provided a ticker

    if len(sys.argv) < 2:
        print(" Error: No ticker symbol provided.")
        sys.exit(1)

    # Replace with your actual keys or use environment variables
    groq_key = os.getenv("GROQ_API_KEY")
    av_key = os.getenv("ALPHA_VANTAGE_API_KEY")

    # Initialize the orchestrator
    manager = FinancialOrchestrator(groq_key=groq_key, av_key=av_key)

    # Test with a ticker
    symbol = sys.argv[1].upper()
    print(f"Starting analysis for {symbol}...")
    result = manager.run_analysis(symbol)
    print(result)


if __name__ == "__main__":
    main()
