import streamlit as st
from PIL import Image


header_image = Image.open("assets/images/banner_escuela_simbad.png")  # reemplaza con tu archivo

# Mostrar la imagen a ancho completo
st.image(header_image, use_column_width=True)

# =====================================================
# Contact Section
# =====================================================
st.header("🧬 Contact")

st.markdown(
    """
If you have any questions or need assistance during the School, you can contact the organizers:
"""
)

st.markdown("[📞 Cristina, +5358413071](tel:+5358413071)")
st.markdown("[📞 David, +5353158490](tel:+5353158490)")

escalinata = Image.open("assets/images/escalinata.jpg")  # reemplaza con tu archivo

# Mostrar la imagen a ancho completo
st.image(escalinata, use_column_width=True)