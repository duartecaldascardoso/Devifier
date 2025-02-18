import requests

import streamlit as st

st.title("EXAMPLE WORKING")

name = st.text_input("Enter your name", "John Doe")
email = st.text_input("Enter your email")
message = st.text_area("Enter your message")

if st.button("Submit"):
    data = {"name": name, "email": email, "message": message}
    response = requests.post("http://127.0.0.1:8000/submit_form", json=data)

    if response.status_code == 200:
        st.success("Form submitted successfully")

    else:
        st.error("Failed to submit form")
