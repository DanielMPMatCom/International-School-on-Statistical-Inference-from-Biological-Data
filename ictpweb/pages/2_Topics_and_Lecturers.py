import streamlit as st
from utils.loaders import load_yaml

st.header("Topics & Lecturers")

topics = load_yaml("data/topics_and_lecturers.yaml")

for topic in topics:
    st.subheader(topic["topic"])
    cols = st.columns(2)

    for i, lecturer in enumerate(topic["lecturers"]):
        cols[i % 2].markdown(f"👤 {lecturer['name']}")

    st.divider()
