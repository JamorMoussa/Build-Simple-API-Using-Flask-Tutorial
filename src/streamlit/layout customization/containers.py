import streamlit as st
import numpy as np

c = st.container()
st.write("This is outside the container 'will be show last'")
c.write("This is inside the container 'will be show first'")

# You can call any Streamlit command, including custom components:
c.bar_chart(np.random.randn(50, 3))
