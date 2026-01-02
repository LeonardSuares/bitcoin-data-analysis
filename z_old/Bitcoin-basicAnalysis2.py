import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import folium
import webbrowser
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px

from plotly.offline import download_plotlyjs, init_notebook_mode, plot


pd.set_option('display.max_columns', None)

import  warnings
from warnings import filterwarnings
filterwarnings("ignore")

df = pd.read_csv(r'C:\Users\leona\PycharmProjects\Python Data Analysis Projects\Bitcoin-dataAnalysis\bitcoin_price_Training - Training.csv')
# print(df.head(5))
# print(df.info())
# print(df.describe().T)

df["Date"] = pd.to_datetime(df["Date"])

df_isnull = df.isnull().sum()
# print(df_isnull)

df_duplicate = df.duplicated().sum()
# print(df_duplicate)

data = df.sort_index(ascending= False).reset_index()

data.drop('index', axis=1, inplace=True)
# print(data.columns)
print(data.shape)

bitcoin_sample = data[0:50]
print(bitcoin_sample)

trace = go.Candlestick(x=bitcoin_sample['Date'],
                       high = bitcoin_sample['High'],
                       open = bitcoin_sample['Open'],
                       close = bitcoin_sample['Close'],
                       low = bitcoin_sample['Low'])

candle_data = [trace]

layout = {
    'title':'Bitcoin Historical Price',
    'xaxis':{'title':'Date'}
}

fig = go.Figure(data = candle_data, layout = layout)
fig.update_layout(xaxis_rangeslider_visible = False)
fig.show()