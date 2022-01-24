import yfinance as yf
import streamlit as st
import pandas as pd

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")
# Here you can use markdown language to make your app prettier
st.write("""
# Financial App
""")

# We will use Amazon stocks
stock = 'AMZN'

# Get stock data
get_stock_data = yf.Ticker(stock)

# Set the time line of your data
ticket_df = get_stock_data.history(period='1d', start='2021-1-02', end='2021-12-12')


# Space out the maps so the first one is 2x the size of the other three
a1, a2 = st.columns((4.5, 1.5))

with a1:
    st.line_chart(ticket_df.Close)
with a2:
    st.bar_chart(ticket_df.Volume)

# Show your data in line chart




# Space out the maps so the first one is 2x the size of the other three
c1, c2 = st.columns((3, 3))

with c1:
    st.bar_chart(ticket_df.Volume)
with c2:
    st.bar_chart(ticket_df.Volume)

c3, c4 = st.columns((4, 2))

with c3:
    st.bar_chart(ticket_df.Volume)
with c4:
    st.text("text")
    st.text("text")
    st.text("text")
    st.text("text")
