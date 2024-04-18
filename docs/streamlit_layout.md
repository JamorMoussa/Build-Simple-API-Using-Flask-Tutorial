# Streamlit Layout Customization Examples

Here are examples demonstrating layout customization in a Streamlit app using commands to arrange widgets and elements in columns, Containers, or sidebars:

## 1. Arranging Widgets in Columns
```python
import streamlit as st

# Arrange widgets in columns
col1, col2 = st.columns(2)

# Add widgets to columns
with col1:
    st.header("Column 1")
    st.write("This is content in column 1.")

with col2:
    st.header("Column 2")
    st.write("This is content in column 2.")
```
![column](../images/layout%20customization/columns.png)

## 2. Arranging Widgets in Containers
```python
import streamlit as st
import numpy as np

c = st.container()
st.write("This is outside the container 'will be show last'")
c.write("This is inside the container 'will be show first'")

# You can call any Streamlit command, including custom components:
c.bar_chart(np.random.randn(50, 3))
```
![Containers](../images/layout%20customization/container.png)

## 3. Arranging Widgets in Sidebars
```python
import streamlit as st

# Arrange widgets in a sidebar
with st.sidebar:
    st.header("Sidebar Header")
    st.write("This is content in the sidebar.")
    st.button("Sidebar Button")
```
![slidbar](../images/layout%20customization/sidebar.png)

## 4. Mixing Columns, Containers, and Sidebars
```python
import streamlit as st
import numpy as np

# Sidebar
with st.sidebar:
    st.header("Sidebar Header")
    st.write("This is content in the sidebar.")
    st.button("Sidebar Button")

# Main content area with columns and rows
st.header("Main Content")
col1, col2 = st.columns([1, 2])

# Add widgets to columns
with col1:
    st.write("This is content in column 1.")

with col2:
    st.write("This is content in column 2.")

c = st.container()
st.write("This is outside the container 'will be show last'")
c.write("This is inside the container 'will be show first'")
```
![mixed](..//images/layout%20customization/mix%20layout.png)

These examples demonstrate how to use simple commands in Streamlit to customize the layout of your app, arranging widgets and elements in columns, rows, or sidebars. You can mix and match these layout options to create the desired structure for your Streamlit app.

For more information and detailed documentation, visit the [Streamlit Documentation](https://docs.streamlit.io/develop/api-reference/layout).


You can copy and paste this markdown content into your `README.md` file in your GitHub repository. Let me know if you need further assistance!