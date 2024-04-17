import streamlit as st

# Text input widget
name = st.text_input('Enter your name', 'John Doe')
st.write('Hello', name)
