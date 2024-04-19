# Streamlit Magic Commands Examples

Here are code examples demonstrating the usage of different magic commands provided by Streamlit:

## 1. st.write():
```python
import streamlit as st

# st.write() example
st.write("This is a Streamlit app.")
```
![st.write](../../images/magic%20commands/st.write.png)

## 2. st.header():
```python
import streamlit as st

# st.header() example
st.header("This is a Header")
```
![st.header](../../images/magic%20commands/st.header.png)

## 3. st.title():
```python
import streamlit as st

# st.title() example
st.title("This is a Title")
```
![st.title](../../images/magic%20commands/st.title.png)

## 4. st.subheader():
```python
import streamlit as st

# st.subheader() example
st.subheader("This is a Subheader")
```
![st.subheader](../../images/magic%20commands/st.subheader.png)

## 5. st.text():
```python
import streamlit as st

# st.text() example
st.text("This is some plain text.")
```
![st.text](../../images/magic%20commands/st.text.png)

## 6. st.markdown():
```python
import streamlit as st

# st.markdown() example
st.markdown("## This is a Markdown title")
```
![st.markdown](../../images/magic%20commands/st.markdown.png)

## 7. st.latex():
```python
import streamlit as st

# st.latex() example
st.latex(r'\sqrt{a^2 + b^2}')
```
![st.latex](../../images/magic%20commands/st.latex.png)

## 8. st.code():
```python
import streamlit as st

# st.code() example
code = '''
def hello():
    print("Hello, Streamlit!")
hello()
'''
st.code(code, language='python')
```
![st.code](../../images/magic%20commands/st.code.png)

## 9. st.json():
```python
import streamlit as st

# st.json() example
json_data = {'name': 'John', 'age': 30}
st.json(json_data)
```
![st.json](../../images/magic%20commands/st.json.png)

## 10. st.table():
```python
import streamlit as st
import pandas as pd

# st.table() example
data = {'Name': ['John', 'Jane', 'Doe'], 'Age': [30, 25, 40]}
df = pd.DataFrame(data)
st.table(df)
```
![st.table](../../images/magic%20commands/st.table.png)

## 11. Combined Usage of All Magic Commands:
```python
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
```
![app](../../images/magic%20commands/app.png)

These examples demonstrate the usage of various Streamlit magic commands. Feel free to explore and customize them as per your requirements.

For more information and detailed documentation, visit the [Streamlit Documentation](https://docs.streamlit.io/develop/api-reference).
```