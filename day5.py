import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# example 1
st.write('Hello, *World* :sunglasses:')

# example 2
st.write('Display numbers')
st.write(1234)

# example 3
st.write('Display DataFrame')
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

# example 4
st.write('Accept multiple arguments')
st.write(f'Below is a DataFrame:', df, 'Above is a dataframe.')

# example 5
a = 'a'
b = 'b'
c = 'c'

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=[a, b, c])

chart = alt.Chart(df2).mark_circle().encode(
    x=a, y=b, size=c, color=c, tooltip=[a, b, c]
)
st.write(chart)
