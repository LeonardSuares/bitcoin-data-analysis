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
import cufflinks as cf
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

cf.go_offline()
data['Close_price_pct_change'] = data['Close'].pct_change()*100
# Reset the index to make 'Date' a regular column for Plotly Express
plot_data = data[['Close_price_pct_change']].reset_index()

# 1. Create the figure using Plotly Express
fig = px.line(
    plot_data,
    x='Date',
    y='Close_price_pct_change',
    title='Bitcoin Daily Close Price Percentage Change (Plotly Express)',
    template="plotly_dark"
)

# You can add custom styling to the y-axis (e.g., set the name)
fig.update_yaxes(title='Daily Change (%)')

# 2. Save the figure to HTML
file_path = 'bitcoin_pct_change_chart.html'
fig.write_html(file_path)

# 3. Open it in the browser
webbrowser.open_new_tab(os.path.abspath(file_path))