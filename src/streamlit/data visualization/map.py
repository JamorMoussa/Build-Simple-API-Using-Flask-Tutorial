import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1000, 2) / [10, 10] + [31.7917, -7.0926],
    columns=['lat', 'lon'])

st.map(df)