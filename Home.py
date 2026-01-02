import streamlit as st
import plotly.express as px
from utils import load_bitcoin_data

st.set_page_config(page_title="Bitcoin Intelligence", layout="wide", page_icon="₿")

st.title("₿ Bitcoin Market Analysis")
data = load_bitcoin_data()

# --- KEY METRICS ---
st.subheader("Market Snapshot")
col1, col2, col3 = st.columns(3)

latest_price = data['Close'].iloc[-1]
prev_price = data['Close'].iloc[-2]
price_diff = latest_price - prev_price
all_time_high = data['High'].max()

col1.metric("Current Price", f"${latest_price:,.2f}", f"{price_diff:+.2f}")
col2.metric("All-Time High", f"${all_time_high:,.2f}")
col3.metric("Data Range", f"{data['Date'].min().year} - {data['Date'].max().year}")

st.divider()

# --- MAIN OVERVIEW CHART ---
st.subheader("Price History (USD)")
fig = px.line(data, x='Date', y='Close', color_discrete_sequence=['#f2a900']) # Bitcoin Gold
fig.update_layout(hovermode="x unified", template="plotly_white")
st.plotly_chart(fig, use_container_width=True)

st.sidebar.success("Select a detailed analysis page above.")