import streamlit as st

# st.code() example
code = '''
def hello():
    print("Hello, Streamlit!")
hello()
'''
st.code(code, language='python')
