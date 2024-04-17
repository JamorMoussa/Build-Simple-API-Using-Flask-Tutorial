import streamlit as st
import altair as alt
import pandas as pd

# Create sample dataframe
data = pd.DataFrame({'x': range(10), 'y': range(10)})

# Plot using Altair
chart = alt.Chart(data).mark_line().encode(x='x', y='y')
chart.properties(title='Altair Example').interactive()
st.write(chart)
