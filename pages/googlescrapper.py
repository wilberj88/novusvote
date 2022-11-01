import pytrends
import pandas as pd
from bs4 import BeautifulSoup
import requests as r
import streamlit as st
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar
import numpy as np
import datetime as dt
from datetime import date
from pytrends.request import TrendReq
from statsmodels.tsa.seasonal import seasonal_decompose
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

# Notebook settings
warnings.filterwarnings("ignore")
pd.set_option('display.max_rows', None)
pytrends = TrendReq(hl='en-US', tz=360)
# sns.set_theme()


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Vote - Diagnóstico", page_icon="🗳️")
st.title('Novus Vote 🗳️')
st.header("Diagnóstico de Campaña y Candidato")
st.write("Análisis de Posicionamiento y Sentimiento en Google")

#SYSTEM
kw_list = ["covid"]
frequency = "daily" # ie. hourly, weekly, monthly, yearly
geo = "US"
hl = "en-US"
# Select Start Date
year_start = 2017
month_start = 6
day_start=1
hour_start=0
# Select End Date
year_end=2020
month_end=6
day_end=30
hour_end=0
#get the trend
google_trends = pytrends.get_historical_interest(kw_list,
 year_start = year_start, 
 month_start = month_start, 
 day_start = day_start, 
 hour_start = hour_start, 
 year_end = year_end, 
 month_end = month_end, 
 day_end = day_end, 
 hour_end = hour_end, 
 cat=0, 
 geo=geo, 
 gprop=’’, 
 sleep=0,
 frequency=frequency)
google_trends = google_trends.reset_index()
google_trends.columns = [‘date’, ‘keyword’,’partial’]
pd.to_datetime(google_trends[‘date’])
google_trends.head()
# Plot google trends over time
sns.set(rc={"figure.figsize":(14, 6)})
sns.lineplot(data=google_trends, x='date', y='keyword')
#desestacionalizado
series = google_trends.set_index('date')
result = seasonal_decompose(series, model='additive', period=365)
result.seasonal.plot()
# Get Google Keyword Suggestions
pytrend = TrendReq()
keywords = pytrend.suggestions(keyword='buy house')
df = pd.DataFrame(keywords)
df



st.write("""
**Credits**
- Software build by `Novus Wilber` with `Bing_Microsoft` data
""")
st.write('---')
