import streamlit as st

st.title("Select Language")
st.write("Choose a language from the sidebar to switch pages.")

# Sidebar navigation (Streamlit detects files in `pages/`)
st.sidebar.success("Select a language from the sidebar.")
