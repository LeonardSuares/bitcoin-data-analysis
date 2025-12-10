import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import folium
import webbrowser
import  chart_studio.plotly as py
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

plt.figure(figsize=(20,12))

for index , col in enumerate (['Open', 'High', 'Low', 'Close'], 1):
    plt.subplot(2,2, index)
    plt.plot(df['Date'], df[col])
    plt.title(col)

plt.show()