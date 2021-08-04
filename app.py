import os
import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports 
from multipage import MultiPage
from pages import data_upload, machine_learning, metadata, data_visualize, redundant # import your pages here

# Create an instance of the app 
app = MultiPage()


st.title("Market open and close analysis")

# Add all your application here
app.add_page("Select symbols", data_upload.app)
app.add_page("Data download", metadata.app)
app.add_page("Exploratory Analysis",data_visualize.app)
app.add_page("Machine Learning", machine_learning.app)

#app.add_page("Y-Parameter Optimization",redundant.app)

# The main app
app.run()
