import streamlit as st
import base64

st.header("Welcome")

st.markdown(
    """
    The **International School on Statistical Inference from Biological Data** is an intensive academic program focused on:

    - Advanced topics
    - Hands-on workshops
    - Interaction with international experts

    📅 **Dates:** February 2-13, 2026  
    📍 **Location:** Havana - Cuba. Universidad de La Habana
    """
)

pdf_path = "assets/posters/winter_school_poster.pdf"

def display_pdf(path: str, width: int = 700, height: int = 900):
    """
    Embed a PDF file in the Streamlit app.

    Parameters
    ----------
    path : str
        Path to the PDF file.
    width : int
        Width of the embedded viewer.
    height : int
        Height of the embedded viewer.
    """
    with open(path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    pdf_display = f"""
        <iframe
            src="data:application/pdf;base64,{base64_pdf}"
            width="{width}"
            height="{height}"
            type="application/pdf">
        </iframe>
    """

    st.markdown(pdf_display, unsafe_allow_html=True)


display_pdf(pdf_path)

st.download_button(
    label="📄 Download poster (PDF)",
    data=open(pdf_path, "rb"),
    file_name="Winter_School_2026_Poster.pdf",
    mime="application/pdf",
)



