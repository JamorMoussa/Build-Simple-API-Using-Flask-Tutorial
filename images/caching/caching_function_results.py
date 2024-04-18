import streamlit as st

# Define a function with expensive computation
@st.cache
def expensive_computation(x):
    # Some expensive computation
    return x * x

# Call the function with different inputs
result1 = expensive_computation(5)
result2 = expensive_computation(5)  # This call will be cached
result3 = expensive_computation(10)

# Display results
st.write("Result 1:", result1)
st.write("Result 2:", result2)
st.write("Result 3:", result3)
