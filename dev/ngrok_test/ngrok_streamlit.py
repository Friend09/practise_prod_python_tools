import streamlit as st
"""
This Streamlit app simulates and visualizes multiple random walks with adjustable slope and noise.

Features:
- Interactive sliders in the sidebar to control the 'slope' (mean) and 'noise' (standard deviation) of the random walk increments.
- Generates a 100-step random walk for 10 series using a cumulative product of normally distributed random values.
- Plots each series on a single matplotlib figure for comparison.
- Displays the plot within the Streamlit app.

Dependencies:
- streamlit
- numpy
- matplotlib

Usage:
Run the script with Streamlit to launch the interactive simulation dashboard.
"""
import numpy as np
import matplotlib.pyplot as plt

st.title("Simulation[tm]")
st.write("Here is our super important simulation")

x = st.sidebar.slider('slope', min_value=0.01, max_value= 0.10, step=0.01)
y = st.sidebar.slider('noise', min_value=0.01, max_value= 0.10, step=0.01)

arr = np.cumprod(1 + np.random.normal(x, y, (100,10)), axis=0)
for i in range(arr.shape[1]):
    plt.plot(arr[:, i])

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
