import streamlit as st

st.set_page_config(
    page_title="International School on Statistical Inference from Biological Data",
    page_icon="❄️",
    layout="wide",
)

st.title("❄️ International School on Statistical Inference from Biological Data")
st.markdown(
    """
    Welcome to the website of the **ICTP International School on Statistical Inference from Biological Data**.
    This platform provides information about the program, topics, lecturers, and speakers.
    
    You can visit the official school page [here](https://indico.ictp.it/event/11113).
    Use the sidebar to navigate through the sections.

    DESCRIPTION:
    The last two decades have witnessed giant experimental breakthroughs in
    different areas of the life sciences, from genomics to epidemiology. Thanks
    to modern high-throughput techniques, biological systems across multiple
    scales -from single molecules up to entire populations- can now be probed
    quantitatively at high spatial and temporal resolutions.These data potentially
    encode a plethora of information about the functional constraints that
    govern its evolution and the physical constraints that limit its performance.
    Extracting this information is also crucial for applications ranging from the
    design of proteins with a desired functionality to the reconstruction of
    contacts during epidemics. Inverse statistical mechanics attempts to do it
    by inferring generative models from data using methods from the physics
    of disordered and random systems but more recently also exploring AI
    approaches. Specific characteristics of biological data however, like strong
    undersampling and heterogeneity, limit the effectiveness of these tools.
    The school will explore the opportunities and limits of statistical inference
    across biological systems and applications.

    DIRECTORS:
    - Andrea De Martino, Politecnico di Torino, Italy
    - Jacopo Grilli, ICTP, Italy
    - Roberto Mulet, University of Havana, Cuba
    """
)
def load_css(path: str):
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("assets/styles/custom.css")
