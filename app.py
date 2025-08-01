import streamlit as st
from st_img_carousel import img_carousel

# Page config
st.set_page_config(page_title="BMW Cars", layout="wide")

# --- Header navigation ---
col1, col2, col3 = st.columns([10, 3, 1])
with col2:
    if st.button("About Us"):
        st.switch_page("pages/about_us.py")
with col3:
    if st.button("Models"):
        st.switch_page("pages/models.py")

# --- Page content ---
st.header("Cars 🚘 - US COUNTRIES")
st.subheader("INTERNATIONAL CARS")

# --- Centered image and text ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("artifact/images/CAR SHOWROOM - AYA DESIGNS.jpg")  # Use forward slashes
    st.write("""
        The fascination of the BMW Group lies not just in our products and technologies 
        but in our history too, which has been written by inventors, pioneers and engineers. 
        Today, the BMW Group is the world s leading manufacturer of premium cars and motorcycles 
        and a provider of premium financial and mobility services. 
        ...
        BMW India Foundation supports initiatives in areas like intercultural innovation, 
        social inclusion, sustainable resource use, skill development, and road safety.
    """)

    # --- Privacy Agreement & Navigation ---
    agree = st.checkbox("I agree to the privacy policy and terms and conditions")

    if agree:
        if st.button("Continue"):
            st.switch_page("pages/my_watches.py")
    else:
        st.warning("Please accept the terms and conditions before continuing.")
