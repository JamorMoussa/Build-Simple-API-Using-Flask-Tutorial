import streamlit as st
import pandas as pd

# st.write() example
st.write("1. This is st.write() example.")

# st.header() example
st.header("2. This is st.header() example")

# st.title() example
st.title("3. This is st.title() example")

# st.subheader() example
st.subheader("4. This is st.subheader() example")

# st.text() example
st.text("5. This is st.text() example.")

# st.markdown() example
st.markdown("6. ## This is a st.markdown() example")

# st.latex() example
st.latex(r"\sqrt{a^2 + b^2}")

# st.code() example
code = '''
def hello():
    print("Hello, Streamlit!")
hello()
'''
st.code("8.This is st.code() example" + code, language='python')

# st.json() example
json_data = {'name': 'mohamed stifi', 'age': 30}
st.json(json_data)

# st.table() example
data = {'Name': ['mohamed', 'stifi', 'hassan'], 'Age': [30, 25, 40]}
df = pd.DataFrame(data)
st.table( df)
