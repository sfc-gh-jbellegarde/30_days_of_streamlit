import streamlit as st

st.header('st.multiselect')

# multiselect with pre-selected items
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)

st.write('You selected:', options)
