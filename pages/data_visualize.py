import streamlit as st
import numpy as np
import pandas as pd
from pages import utils
import matplotlib.pyplot as plt
import seaborn as sns
import os

def app():
    if 'main_data.csv' not in os.listdir('data'):
        st.markdown("Please upload data through `Upload Data` page!")
    else:

        st.write("### Analysis of spread between trades and quotes")

        # df_analysis = pd.read_csv('data/2015.csv')
        df_analysis = pd.read_csv('data/stock_data.csv')

        st.line_chart(df_analysis[['Open', 'Close']])

        st.line_chart(df_analysis[['Open', 'Volume']])

        