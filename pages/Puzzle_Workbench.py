import requests
import streamlit as st

st.title("Puzzle Workbench")

with st.form("Create a new Puzzle"):
    name = st.text_input("Name")
    description = st.text_area("Description")
    image = st.text_input("Image Path")
    eloRating = st.number_input("Elo Rating", value=1000)
    answer = st.text_input("Answer")
    hint = st.text_input("Hint")
    puzzleType = st.selectbox("Puzzle Type", ["Open Answer", "Multiple Choice"])
    submitted = st.form_submit_button("Create Puzzle")

    if submitted:
        data = {
            "name": name,
            "description": description,
            "image": image,
            "eloRating": eloRating,
            "answer": answer,
            "hint": hint,
            "puzzleType": puzzleType,
        }
        response = requests.post(
            "http://localhost:8000/create_puzzle",
            json=data,
        )

        if response.status_code == 200:
            st.toast("Form submitted successfully")

        else:
            st.toast("Failed to submit form")
