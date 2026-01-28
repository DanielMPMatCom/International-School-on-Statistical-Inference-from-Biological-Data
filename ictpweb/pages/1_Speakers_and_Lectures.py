import streamlit as st
from PIL import Image
from utils.loaders import load_yaml


header_image = Image.open("assets/images/banner_escuela_simbad.png")  # reemplaza con tu archivo

# Mostrar la imagen a ancho completo
st.image(header_image, use_column_width=True)

st.header("Speakers and Lectures")
lecture_blocks = load_yaml("data/lectures.yaml")

for block in lecture_blocks:
    # Construir encabezado con speakers
    header = ", ".join(
        f"{l['name']} ({l.get('affiliation', '')})"
        if "affiliation" in l
        else l["name"]
        for l in block["lecturers"]
    )

    with st.expander(header):
        for lec in block["lectures"]:
            label = lec.get("label", "")
            title = lec["title"]
            subtitle = lec.get("subtitle", "")
            note = lec.get("note", "")

            if label:
                st.markdown(f"**{label}**: {title}")
            else:
                st.markdown(f"**{title}**")

            if subtitle:
                st.caption(subtitle)

            if note:
                st.caption(f"({note})")

            st.write("")


einstein = Image.open("assets/images/einstein.jpg")  # reemplaza con tu archivo

# Mostrar la imagen a ancho completo
st.image(einstein, use_column_width=True)

