import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

# removes the need to do
# chart = alt.Chart(df2).mark_circle().encode(
# x=a, y=b, size=c, color=c, tooltip=[a, b, c]
st.line_chart(chart_data)
