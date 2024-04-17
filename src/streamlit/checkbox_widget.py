import streamlit as st

# Checkbox widget
agree = st.checkbox('I agree to the terms and conditions')
if agree:
    st.write('Thank you for agreeing!')
