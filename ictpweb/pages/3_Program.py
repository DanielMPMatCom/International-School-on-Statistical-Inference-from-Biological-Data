import streamlit as st
from utils.loaders import load_yaml

st.header("Program")

program = load_yaml("data/program.yaml")

for day in program:
    with st.expander(f"{day['day']} – {day['title']}"):
        for session in day["sessions"]:
            st.write(f"🕒 {session['time']} — {session['topic']}")
