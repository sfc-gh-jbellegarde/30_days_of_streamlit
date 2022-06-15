import streamlit as st

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6FD1"
textColor="#FFFFFF"
font="sans serif"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write(f'Selected number from slider widget is: {number}')
