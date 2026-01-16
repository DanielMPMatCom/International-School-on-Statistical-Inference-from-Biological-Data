import streamlit as st
from utils.loaders import load_yaml

st.header("Speakers")

lecturers = load_yaml("data/speakers.yaml")

for lecturer in lecturers:
    st.subheader(lecturer["name"])
    st.caption(f"{lecturer['affiliation']}, {lecturer['country']}")
    st.divider()
