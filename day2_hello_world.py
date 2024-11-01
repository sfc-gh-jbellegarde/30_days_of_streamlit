# Import python packages
import streamlit as st

# Inject Google Tag Manager script
st.markdown(
    """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-6NXDHHH86G"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-6NXDHHH86G');
    </script>
    """,
    unsafe_allow_html=True
)

st.header("Hello World!")