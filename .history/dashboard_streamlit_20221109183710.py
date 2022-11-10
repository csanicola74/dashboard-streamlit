"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


"""
Along with magic commands, st.write() is Streamlit's "Swiss Army knife". 
You can pass almost anything to st.write(): text, data, Matplotlib figures, Altair charts, and more. 
Don't worry, Streamlit will figure it out and render things the right way.
"""

# draw a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# plot a map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

# widgets
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# access widgets by a key
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

# checkboxes to show/hide data
