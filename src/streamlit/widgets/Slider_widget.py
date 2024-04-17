import streamlit as st

# Slider widget
age = st.slider('Select your age', 0, 100, 25)
st.write('Your age is:', age)
