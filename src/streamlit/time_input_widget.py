import streamlit as st

# Time input widget
import datetime
time = st.time_input('Set an alarm for', datetime.time(8, 30))
st.write('Alarm set for:', time)
