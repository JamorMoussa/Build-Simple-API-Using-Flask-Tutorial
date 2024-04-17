
import streamlit as st
import pandas as pd

# st.table() example
data = {'Name': ['mohamed', 'stifi', 'hassan'], 'Age': [20, 22, 40]}
df = pd.DataFrame(data)
st.table(df)
