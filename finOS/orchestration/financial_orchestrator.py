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
import json

from agents.harvester import HarvesterAgent
from agents.quant import QuantAgent
from agents.strategist import StrategistAgent


class FinancialOrchestrator:
    def __init__(self, groq_key, av_key):
        """
        Initializes the orchestration layer
        """

        self.harvester = HarvesterAgent(api_key=av_key)
        self.quant = QuantAgent()
        self.strategist = StrategistAgent(api_key=groq_key)

    def run_analysis(self, symbol):
        """
        Orchestrates agentic workflow
        """

        vitals = self.harvester.get_market_vitals(symbol)

        proj_price, proj_pct = self.quant.calculate_6month_projection(symbol)
        math_results = {"price": proj_price, "pct": proj_pct}

        final_report_json = self.strategist.analyze_vitals(vitals, math_results)

        try:
            return json.loads(final_report_json)
        except json.JSONDecodeError:
            return {
                "error": "Failed to parse strategist report",
                "raw": final_report_json,
            }
