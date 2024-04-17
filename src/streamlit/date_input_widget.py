import streamlit as st

# Date input widget
import datetime
today = st.date_input('Today is', datetime.date.today())
st.write('Selected date:', today)