import streamlit as st
import pandas as pd

# Define a function to load data
@st.cache
def load_data(filename):
    # Some expensive data loading operation
    data = pd.read_csv(filename)
    return data

# Load data from file
filename = "data.csv"
data = load_data(filename)

# Display the loaded data
st.write(data)
