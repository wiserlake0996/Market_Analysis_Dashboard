import streamlit as st
import numpy as np
import pandas as pd
from pages import utils
import matplotlib.pyplot as plt
import seaborn as sns
import os
import yfinance as yf

def app():
    if 'main_data.csv' not in os.listdir('data'):
        st.markdown("Please upload data through `Upload Data` page!")
    else:

        st.write("### Analysis of spread between trades and quotes")

        # df_analysis = pd.read_csv('data/2015.csv')
        df_analysis = pd.read_csv('data/main_data.csv')
        df_analysis = yf.download("AAPL", start="2019-01-01", end="2019-04-30")

        st.line_chart(df_analysis[['Open', 'Close']])

        st.line_chart(df_analysis[['Open', 'Volume']])

        