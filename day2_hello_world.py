# Import python packages
import streamlit as st
import streamlit.components.v1 as components

components.html(
    """
    <head>
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-6NXDHHH86G"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());

          gtag('config', 'G-6NXDHHH86G');
        </script>
    </head>
    """,
    height=0
)

st.header("Hello World!")