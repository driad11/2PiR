import streamlit as st

st.title("Calculator test")

# Get user input
first = st.slider("Enter first number", min_value =0, max_value=100, value=50)
second = st.slider("Enter second number", min_value =0, max_value=100, value=50)

# Perform calculation when user clicks button
if st.button("Calculate Sum"):
    result = first + second
    st.success(f"Equals: {result}")
