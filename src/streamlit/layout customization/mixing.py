import streamlit as st
import numpy as np

# Sidebar
with st.sidebar:
    st.header("Sidebar Header")
    st.write("This is content in the sidebar.")
    st.button("Sidebar Button")

# Main content area with columns and rows
st.header("Main Content")
col1, col2 = st.columns([1, 2])

# Add widgets to columns
with col1:
    st.write("This is content in column 1.")

with col2:
    st.write("This is content in column 2.")

c = st.container()
st.write("This is outside the container 'will be show last'")
c.write("This is inside the container 'will be show first'")

