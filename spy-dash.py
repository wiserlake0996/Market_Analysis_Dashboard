import yfinance as yf
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from ta.volatility import BollingerBands
from ta.trend import MACD
from ta.momentum import RSIIndicator

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")
# Here you can use markdown language to make your app prettier
st.write("""
# Financial App
""")

###########
# sidebar #
###########

st.markdown(f'''
    <style>
        section[data-testid="stSidebar"] .css-ng1t4o {{width: 14rem;}}
        section[data-testid="stSidebar"] .css-1d391kg {{width: 14rem;}}
    </style>
''',unsafe_allow_html=True)
option = st.sidebar.selectbox('Select one symbol', ( 'DIA', 'QQQ',"SPY",'IWM'))

import datetime
today = datetime.date.today()
before = today - datetime.timedelta(days=700)
start_date = st.sidebar.date_input('Start date', before)
end_date = st.sidebar.date_input('End date', today)
if start_date < end_date:
    st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.sidebar.error('Error: End date must fall after start date.')





##############
# Stock data #
##############

# Download data
df = yf.download(option,start= start_date,end= end_date, progress=False)

# Bollinger Bands
indicator_bb = BollingerBands(df['Close'])
bb = df
bb['bb_h'] = indicator_bb.bollinger_hband()
bb['bb_l'] = indicator_bb.bollinger_lband()
bb = bb[['Close','bb_h','bb_l']]

# Moving Average Convergence Divergence
macd = MACD(df['Close']).macd()

# Resistence Strength Indicator
rsi = RSIIndicator(df['Close']).rsi()













# We will use Amazon stocks
stock = 'AMZN'

# Get stock data
get_stock_data = yf.Ticker(stock)

# Set the time line of your data
ticket_df = get_stock_data.history(period='1d', start='2021-1-02', end='2021-12-12')


# Space out the maps so the first one is 2x the size of the other three
a1, a2 = st.columns((4, 2))

with a1:
    # Plot the prices and the bolinger bands
    st.write('Stock Bollinger Bands')
    st.line_chart(bb)
with a2:
    # Data of recent days
    st.write('Recent data ')
    st.dataframe(df.tail(10))

# Show your data in line chart




# Space out the maps so the first one is 2x the size of the other three
c1, c2 = st.columns((3, 3))

with c1:
    st.write('Stock Moving Average Convergence Divergence (MACD)')
    st.area_chart(macd)
with c2:
    st.write('Stock RSI ')
    st.line_chart(rsi)

c3, c4 = st.columns((4, 2))

with c3:
    st.bar_chart(ticket_df.Volume)
with c4:
    st.text("text")
    st.text("text")
    st.text("text")
    st.text("text")
