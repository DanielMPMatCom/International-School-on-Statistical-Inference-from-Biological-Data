import streamlit as st
from PIL import Image


header_image = Image.open("assets/images/banner_escuela_simbad.png")  # reemplaza con tu archivo

# Mostrar la imagen a ancho completo
st.image(header_image, use_column_width=True)

# Título de la página
st.title("Logistics - Winter School Havana")

# =====================================================
# Accommodation Section
# =====================================================
st.header("Student Accommodation")
st.markdown(
    """
**For students coming from Latin America through ICTP:**  

- **Place:** Rocinante Guest House  
- **Address:** 21 and G streets, Vedado, Plaza de la Revolución, Havana  
- **Room:** 2-bedroom rooms with bathroom  
- **Meals:** Breakfast included  
- **Linens:** Provided, no need to bring your own  

> This is a modest but comfortable motel near the University.
"""
)

# =====================================================
# Currency Section
# =====================================================
st.header("Currency and Payments")
st.markdown(
    """
- **Cuban Currency:** Cuban Peso (CUP)  
  - Exchange rate: 1 USD ≈ 460 CUP  
- **Cash is King:** Bring USD or EUR in cash. Cards (Visa/Mastercard) may **not work** or work at inconvenient rates.  
- **Where to exchange money:** At the airport or at Cadeca offices. Exchange small amounts first (~30–50 USD) to start.  
- **Examples of costs:**  
  - Taxi from airport to Vedado: ~25 USD  
  - Cheap lunch near the University: 0.7-4 USD (Pizza or dish with meat, rice, drink, coffee)  
- **Meals at Rocinante:** Breakfast included, likely dinner too, but for variety you may want to dine outside.  
"""
)

# =====================================================
# Safety Section
# =====================================================
st.header("Safety in Cuba")
st.markdown(
    """
Cuba is generally a **safe country** with low violent crime.  
However, take usual precautions:  

**Avoid:**  
- Leaving your bag unattended  
- Exchanging money on the street  
- Buying items from random people offering "good deals" (e.g., cigars from the Habano fair)  
"""
)

# =====================================================
# Health Section
# =====================================================
st.header("Health Advice")
st.markdown(
    """
- Bring **mosquito repellent**  
- Stay hydrated and take general health precautions
"""
)

# =====================================================
# Fun & Extra Activities Section
# =====================================================
st.header("Extra-curricular Activities")
st.markdown(
    """
A set of extra activities will be proposed during the week.  

**Sunday 1st:** Jazz Concert at the National Theater.  
- Organizers have some free tickets.  
- **If interested:** Contact the organizers directly.
"""
)

havana = Image.open("assets/images/havana.jpg")  # reemplaza con tu archivo

# Mostrar la imagen a ancho completo
st.image(havana, use_column_width=True)

