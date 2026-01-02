import streamlit as st
import plotly.express as px
import numpy as np
from utils import load_bitcoin_data

st.title("📈 Resampling & Growth Trends")
data = load_bitcoin_data().set_index('Date')

# --- RESAMPLING SECTION ---
st.subheader("Aggregated Performance")
time_frame = st.selectbox("Select Resampling Frequency", ['Yearly', 'Quarterly', 'Monthly'])
freq_map = {'Yearly': 'YE', 'Quarterly': 'QE', 'Monthly': 'ME'}

resampled_data = data['Close'].resample(freq_map[time_frame]).mean().reset_index()

fig_resampled = px.bar(resampled_data, x='Date', y='Close',
                       title=f"{time_frame} Average Price",
                       color_discrete_sequence=['#4dabf7'])
st.plotly_chart(fig_resampled, use_container_width=True)

st.divider()

# --- LOG SCALING SECTION ---
st.subheader("Exponential Growth (Log Scale)")
col1, col2 = st.columns(2)

with col1:
    fig_norm = px.line(data.reset_index(), x='Date', y='Close', title="Normal Scale")
    st.plotly_chart(fig_norm, use_container_width=True)

with col2:
    # Log scale helps see growth rates more clearly
    data['Log_Close'] = np.log1p(data['Close'])
    fig_log = px.line(data.reset_index(), x='Date', y='Log_Close',
                      title="Log Scale", color_discrete_sequence=['#fd7f6f'])
    st.plotly_chart(fig_log, use_container_width=True)