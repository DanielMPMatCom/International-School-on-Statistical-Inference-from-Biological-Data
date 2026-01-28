import streamlit as st
import pandas as pd
from utils.loaders import load_yaml
from PIL import Image


header_image = Image.open("assets/images/banner_escuela_simbad.png")  # reemplaza con tu archivo

# Mostrar la imagen a ancho completo
st.image(header_image, use_column_width=True)

st.header("Program")

program = load_yaml("data/program.yaml")
# aliases = load_yaml("data/speaker_aliases.yaml")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for week in program:
    st.subheader(week["week"])

    table = []

    for time, row in week["schedule"].items():
        row_data = {"Time": time}
        for day in days:
            cell = row.get(day, "")
            # if cell in aliases:
            #     cell = f"{cell}\n({aliases[cell]})"
            row_data[day] = cell
        table.append(row_data)

    df = pd.DataFrame(table)
    df = df.set_index("Time")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=False
    )


edificio = Image.open("assets/images/facultadedificio.jpg")  # reemplaza con tu archivo

# Mostrar la imagen a ancho completo
st.image(edificio, use_column_width=True)