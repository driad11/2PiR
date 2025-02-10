import streamlit as st

st.set_page_config(page_title="Select Language", layout="wide")

# Hide the default sidebar navigation
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {display: none;}
    </style>
""", unsafe_allow_html=True)

st.title("Select Language")
st.write("Choose a language from the dropdown below to switch pages.")

# Custom page selector
page = st.selectbox("Select Language", ["English", "Deutsch", "Magyar"])

# Redirect users manually
if page == "English":
    st.switch_page("pages/english.py")
elif page == "Deutsch":
    st.switch_page("pages/deutsch.py")
elif page == "Magyar":
    st.switch_page("pages/magyar.py")
