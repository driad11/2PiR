import streamlit as st


st.title("Select language, Sprach auswahl, válasszon nyelvet")

#language selection
language = st.selectbox("select language", ["english", "deutsch" ,"magyar"])

#different pages based on selection
if language == "english":
    st.header("Welcome!")
    st.write("this is the english version.")
elif language == "deutsch":
    st.header("Willkommen!")
    st.write("dies ist die deutsche version.")
elif language == "magyar":
    st.header("Üdvözöljük!")
    st.write("ez az oldal magyar verziója.")
