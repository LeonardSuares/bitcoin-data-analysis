from unittest.mock import inplace

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
# print(data.head(20))
# close = data['Close'].plot()
# plt.show()
data = data.set_index('Date')
# print(data.head(20))
# close = data['Close'].plot()
# plt.show()

#plotting charts side by side for No scaling and log scaling
# plt.figure(figsize=(16,6))
#
# plt.subplot(1,2,1)
# data['Close'].plot()
# plt.title('No Scaling')
#
# plt.subplot(1,2,2)
# np.log1p(data['Close']).plot()
# plt.title('Log Scaling')
# plt.yscale('log')
#
# plt.show()

# Analyzing closing price on a Yearly, Quarterly, Monthly basis
plt.figure(figsize=(18,18))

plt.subplot(2,2,1)
data['Close'].resample('Y').mean().plot()
plt.title(
    'Year',
    # --- ADD THIS PARAMETER ---
    bbox={'facecolor': 'lightgray', 'alpha': 0.6, 'pad': 4}
)

plt.subplot(2,2,2)
data['Close'].resample('Q').mean().plot()
plt.title(
    'Quater',
    # --- ADD THIS PARAMETER ---
    bbox={'facecolor': 'lightgray', 'alpha': 0.6, 'pad': 4}
)

plt.subplot(2,2,3)
data['Close'].resample('M').mean().plot()
plt.title(
    'Month',
    # --- ADD THIS PARAMETER ---
    bbox={'facecolor': 'lightgray', 'alpha': 0.6, 'pad': 4}
)

plt.subplot(2,2,4)
data['Close'].resample('D').mean().plot()
plt.title(
    'Day',
    # --- ADD THIS PARAMETER ---
    bbox={'facecolor': 'lightgray', 'alpha': 0.6, 'pad': 4}
)

plt.show()