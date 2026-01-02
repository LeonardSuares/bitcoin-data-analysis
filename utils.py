import pandas as pd
import streamlit as st


@st.cache_data
def load_bitcoin_data():
    # Load the data from the new folder structure
    df = pd.read_csv("data/bitcoin_price.csv")

    # 1. Cleaning: Dates
    df["Date"] = pd.to_datetime(df["Date"])

    # 2. Sort by date (Oldest to Newest) for time-series charts
    df = df.sort_values(by="Date").reset_index(drop=True)

    # 3. Calculated Columns
    df['Close_pct_change'] = df['Close'].pct_change() * 100

    return df