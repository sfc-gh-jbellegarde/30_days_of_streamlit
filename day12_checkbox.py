import streamlit as st

st.header('st.checkbox')

st.write('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

# actually, I was wrong. if we use if-elif-else, the checkbox will still go through, however the printed statement
# will be the first selected option, even if we choose the other options afterward
if icecream:
    st.write("Great! Here's some more 🍦")

if coffee:
    st.write("Okay, here's some coffee ☕")

if cola:
    st.write("Here you go 🥤")
