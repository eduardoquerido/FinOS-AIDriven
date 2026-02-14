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

from groq import Groq


class StrategistAgent:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def analyze_vitals(self, vitals, math_data):
        """
        Takes data from Harvester and Quant, then reasons with Groq.
        """
        print(f"--- Strategist Agent: Synthesizing report for {vitals['symbol']} ---")

        # prompt = f"""
        #     You are a Financial Strategist. Analyze the following data for {vitals['symbol']}.

        #     TECHNICAL DATA:
        #     - Price: ${vitals['price']}
        #     - Math Projection (6mo): ${math_data['price']} ({math_data['pct']}% change)

        #     NEWS:
        #     - {" ".join(vitals['headlines'])}

        #     TASK:
        #     Compare the math with the news. Generate a final 6-month outlook.
        #     Output ONLY valid JSON.
        #     """
        prompt = f"""
            SYSTEM ROLE:
            You are an expert Financial Quant Strategist. Your goal is to synthesize raw technical data with market sentiment to provide a high-fidelity 6-month price projection.

            INPUT DATA FOR {vitals['symbol']}:
            - Current Spot Price: ${vitals['price']}
            - Statistical Trend (180-day Linear Regression): ${math_data['price']} ({math_data['pct']}% change)
            - Market Intelligence (News Headlines): 
            {" ".join(vitals['headlines'])}

            TASK:
            1. INTERNAL ANALYSIS: Evaluate if the news headlines validate or contradict the mathematical trend.
            2. SENTIMENT SCORING: Assign a label (Bullish, Bearish, or Neutral).
            3. PRICE ADJUSTMENT: If the news is significant, adjust the math-based projection price to reflect reality.
            4. CONFIDENCE: Rate your conviction in this projection from 0-100%.

            OUTPUT FORMAT:
            Return ONLY valid JSON. Do not include conversational text.
            {{
                "symbol": "{vitals['symbol']}",
                "current_price": {vitals['price']},
                "statistical_projection": {math_data['price']},
                "final_projection_price": float,
                "expected_return_pct": float,
                "market_sentiment": "Bullish" | "Bearish" | "Neutral",
                "sentiment_logic": "Explain why you adjusted the math based on the news.",
                "confidence_score": integer
            }}
        """

        completion = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"},
        )
        return completion.choices[0].message.content
