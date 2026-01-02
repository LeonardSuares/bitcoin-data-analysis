import streamlit as st
import plotly.graph_objects as go
from utils import load_bitcoin_data

st.title("🕯️ Historical Candlestick Analysis")
data = load_bitcoin_data()

# Let users choose how many days to look at
days = st.slider("Select number of recent days to view", 30, 500, 100)
recent_data = data.tail(days)

st.subheader(f"Price Action: Last {days} Days")

fig = go.Figure(data=[go.Candlestick(
    x=recent_data['Date'],
    open=recent_data['Open'],
    high=recent_data['High'],
    low=recent_data['Low'],
    close=recent_data['Close'],
    increasing_line_color= '#26a69a', decreasing_line_color= '#ef5350'
)])

fig.update_layout(xaxis_rangeslider_visible=False, template="plotly_white", height=600)
st.plotly_chart(fig, use_container_width=True)

with st.expander("View Raw Historical Data"):
    st.dataframe(recent_data.sort_values(by="Date", ascending=False), use_container_width=True)