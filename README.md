# ₿ Bitcoin Market Intelligence Dashboard

An interactive, multi-page data analysis platform built with **Streamlit** and **Plotly** to visualize historical Bitcoin price action, growth trends, and market volatility. This project transforms raw financial data into a high-fidelity tool for technical analysis.

---

## Key Features

* **Interactive Candlestick Charts:** High-performance price action visualization with a custom date-range slider to inspect specific market cycles.
* **Multi-Timeframe Resampling:** Toggle between **Yearly**, **Quarterly**, and **Monthly** views to identify long-term macro trends vs. short-term noise.
* **Logarithmic Growth Analysis:** Compare standard linear price action against **Logarithmic Scaling** to better visualize exponential growth phases.
* **Volatility Tracking:** Automated calculation and visualization of **Daily Percentage Changes** in closing prices.
* **Real-Time KPIs:** Instant metrics for Current Price, All-Time High, and Price Delta on the landing page.

---

## Tech Stack

* **Language:** `Python 3.x`
* **Dashboarding:** `Streamlit`
* **Data Manipulation:** `Pandas`, `NumPy`
* **Visualization:** `Plotly Graph Objects`, `Plotly Express`
* **ETL Logic:** Centralized data processing in `utils.py` with `@st.cache_data` for optimized performance.

---

## Project Structure

```text
Bitcoin-Analysis/
├── Home.py               # Landing page with market KPIs and price overview
├── utils.py              # Centralized ETL, data cleaning, and date parsing
├── data/
│   └── bitcoin_price.csv # Historical Bitcoin dataset (OHLCV)
└── pages/                # Sidebar-managed analysis modules
    ├── 1_Historical_Analysis.py
    └── 2_Trends_and_Scaling.py
