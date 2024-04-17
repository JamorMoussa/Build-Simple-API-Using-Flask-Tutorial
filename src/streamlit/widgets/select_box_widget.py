import streamlit as st

# Select box widget
option = st.selectbox('Choose an option', ['Option 1', 'Option 2', 'Option 3'])
st.write('You selected:', option)
