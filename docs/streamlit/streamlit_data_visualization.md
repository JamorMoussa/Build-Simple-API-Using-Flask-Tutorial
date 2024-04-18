# Interactive Data Visualization with Streamlit

Here are examples demonstrating how to create interactive charts, graphs, and maps using popular data visualization libraries such as Matplotlib and Altair within Streamlit:

## 1. Matplotlib
```python
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Generate some random data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot using Matplotlib
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Matplotlib Example')
st.pyplot(fig)
```
![matplotlib](../images/data%20visualization/matplotlib.png)

## 2. Altair
```python
import streamlit as st
import altair as alt
import pandas as pd

# Create sample dataframe
data = pd.DataFrame({'x': range(10), 'y': range(10)})

# Plot using Altair
chart = alt.Chart(data).mark_line().encode(x='x', y='y')
chart.properties(title='Altair Example').interactive()
st.write(chart)
```
![altair](../images/data%20visualization/altair.png)

## 3. Map
```python
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1000, 2) / [10, 10] + [31.7917, -7.0926],
    columns=['lat', 'lon'])

st.map(df)
```
![map](../images/data%20visualization/map.png)

## 4. Graph
```python
import streamlit as st
st.graphviz_chart('''
    digraph {
        while -> condetion
        condetion -> true
        condetion -> false
        true -> while_body
        while_body -> condetion
        false -> end
    }
''')
```
![graph](../images/data%20visualization/graph.png)

These examples showcase how to integrate Matplotlib and Altair visualizations into Streamlit apps. You can customize these examples further based on your specific data and visualization requirements. Additionally, Streamlit supports other popular visualization libraries like Bokeh and Plotly, so you can explore those as well if needed.

For more information and detailed documentation, visit the [Streamlit Documentation](https://docs.streamlit.io/develop/api-reference/charts).
