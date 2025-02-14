import streamlit as st


#page config
st.set_page_config(page_title="2PiR", layout="wide")



# Hide the default sidebar navigation
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {display: none;}
    </style>
""", unsafe_allow_html=True)

st.title("Select Language")
st.write("Choose a language from the dropdown below to switch pages.")

# Custom navigation
page = st.selectbox("Select Language", ["English", "Deutsch", "Magyar"])

if page == "English":
    st.switch_page("pages/english.py")
elif page == "Deutsch":
    st.switch_page("pages/deutsch.py")
elif page == "Magyar":
    st.switch_page("pages/magyar.py")
