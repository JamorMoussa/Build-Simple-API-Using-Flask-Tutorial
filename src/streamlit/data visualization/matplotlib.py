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
