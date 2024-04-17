import streamlit as st

# Arrange widgets in columns
col1, col2 = st.columns(2)

# Add widgets to columns
with col1:
    st.header("Column 1")
    st.write("This is content in column 1.")

with col2:
    st.header("Column 2")
    st.write("This is content in column 2.")
