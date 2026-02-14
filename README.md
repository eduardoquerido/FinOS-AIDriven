# FinOS: AI-Driven Financial Orchestrator

**FinOS** is a multi-agent financial intelligence system designed to synthesize real-time market data, historical technical trends, and global news sentiment. By bridging **Scikit-Learn’s** quantitative modeling with **Groq’s** ultra-fast Llama 3 reasoning, FinOS provides a weighted 6-month price projection for any given ticker.

---

## 🚀 The Architecture

FinOS is built on a modular, agentic framework where each agent serves a specific cognitive function:

1. **Harvester Agent (Perception):** Fetches real-time market vitals and technical indicators via Alpha Vantage / Yahoo Finance, and scrapes the latest financial headlines.
2. **Quant Agent (Mathematics):** Uses `scikit-learn` (Linear Regression) to analyze the last 252 trading days and project a statistical "best-fit" price for the next 6 months.
3. **Strategist Agent (Reasoning):** Powered by **Groq**, this agent weighs the "Math Projection" against "News Sentiment" to produce a final, context-aware financial report.

### 📈 Methodology: Hybrid Intelligence

FinOS does not rely solely on AI "guesses." It uses a Hybrid Intelligence approach:

1. **The Baseline:** A Linear Regression model calculates $$y = mx + b$$ based on a 1-year lookback.
2. **The Adjustment:** The LLM acts as a "Risk Manager," adjusting the baseline based on high-impact news (e.g., interest rate hikes, earnings misses, or geopolitical events).

---

## 📂 Project Structure

```text
FinOS-AIDriven/         # Project Root
├── finos/              # Source Code Package
│   ├── agents/
│   │   ├── harvest/    # Perception: Data ingestion & News scraping
│   │   ├── quant/      # Math: Sklearn Linear Regression models
│   │   └── strategist/ # Logic: Groq LLM integration
│   ├── orchestration/  # The "Brain": Coordinates agent workflows
│   └── main.py         # Entry point for the CLI tool
```

### Prerequisites
* Alpha Vantage Api Key
* Groq Api Key
* Python 3.11+ (3.11.14 recommended)

### Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/eduardoquerido/FinOS-AIDriven.git
    cd FinOS-AIDriven
    ```

2. **Set Up Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt -r dev-requiremets.txt
    ```

4. **Configure Environment Variables**

    Create a `.env` file, change `env_example` file or export your keys:

    ```bash
    export GROQ_API_KEY="your_groq_key_here"
    export AV_API_KEY="your_alpha_vantage_key_here"
    ```


### 🚦 Usage

To run the full orchestration for a specific ticker (e.g., VOO, NVDA, BTC):

```bash
python -m main <TICKER>
```

The system will output a structured JSON report similar to this:

```json
{
    "symbol": "VOO",
    "current_price": 512.43,
    "statistical_projection": 545.20,
    "final_projection_price": 538.10,
    "market_sentiment": "Bullish",
    "sentiment_logic": "Math suggests a 6% gain, but recent news regarding inflation spikes suggests a slightly more conservative growth path.",
    "confidence_score": 85
}
```

## 🛠️ Development Automation with Tox

This project uses **[tox](https://tox.wiki/)** to automate environment management, code formatting, and testing.

### Core Commands

| Command | Description |
| :--- | :--- |
| `tox -l` | List all available environments. |
| `tox -a` | List environments with detailed descriptions. |
| `tox` | Run the full suite (formatting, linting, and tests). |
| `tox -e format` | **Auto-fix** code style using `black` and `isort`. |
| `tox -e checklint` | **Verify** code style and import sorting (checks only). |
| `tox -e unittesting` | Run all unit tests in a clean Python 3.10 environment. |

### Maintenance & Troubleshooting

* **Rebuild environments:** Use this if you've updated dependencies or the `tox.ini` file.
  ```bash
  tox -r

## 🔒 Security & Reproducibility
This project uses `pip-tools` to ensure deterministic builds. 
To regenerate the hashed dependencies, run:
`pip-compile --generate-hashes --output-file=requirements.txt requirements.in`

## 🗺️ Roadmap

- [x] **Phase 1:** Data Harvesting & Technicals
- [x] **Phase 2:** Sklearn & Groq Orchestration
- [ ] **Phase 3:** Next.js Dashboard & Visual Charting
- [ ] **Phase 4:** Multi-Ticker Portfolio Monitoring

## ⚖️ License

Copyright (C) 2026 FinOS - Eduardo Querido

This program is free software: you can redistribute it and/or modify it under the terms of the **GNU General Public License** as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but **WITHOUT ANY WARRANTY**; without even the implied warranty of **MERCHANTABILITY** or **FITNESS FOR A PARTICULAR PURPOSE**. See the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.txt) for more details.

---

### 🛡️ Commercial Use & Dual Licensing
The GPLv3 is a strong copyleft license that requires any derivative work to also be open-sourced under the same terms. If your organization requires using **FinOS** in a proprietary, closed-source environment, please contact the author to negotiate a **Commercial License**.