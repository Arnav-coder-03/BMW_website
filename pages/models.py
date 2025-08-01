'''import streamlit as st
 
# Title and intro
st.title("🚗 BMW Car Showcase")
st.subheader("Select a BMW model to view its image")

# Dictionary of models and corresponding image paths
image_files = {
    "BMW M4": "images\pexels-04iraq-1272398525-31041580.jpg",
    "BMW M5": "images\pexels-dbaler-13627418.jpg",
    "BMW M3": "images\pexels-egeardaphotos-2148533277-30433742.jpg"
}

# Model selection dropdown
selected_name = st.selectbox("Choose a model", list(image_files.keys()))

# Display selected image centered in layout
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(
        image_files[selected_name],
        caption=selected_name,
        use_column_width=True
    )'''


import streamlit as st
from PIL import Image
import warnings
warnings.filterwarnings("ignore")


st.set_page_config(page_title="BMW i Series", layout="wide")
st.title("🚘 BMW i Series")
st.subheader("Explore BMW's latest electric models")

# Car data
cars = [
    {
        "name": "THE BMW iX1 LONG WHEELBASE",
        "image": "artifact/images/pexels-04iraq-1272398525-31041580.jpg",
        "fuel": "Full-Electric",
        "price": "₹ 49,00,000",
        "new": True
    },
    {
        "name": "THE NEW ALL-ELECTRIC BMW iX xDRIVE50",
        "image": "artifact/images\pexels-dbaler-13627418.jpg",
        "fuel": "Full-Electric",
        "price": "₹ 1,39,50,000",
        "new": True
    },
    {
        "name": "THE FULLY ELECTRIC BMW i4",
        "image": "artifact/images\pexels-egeardaphotos-2148533277-30433742.jpg",
        "fuel": "Full-Electric",
        "price": "₹ 72,50,000",
        "new": False
    },
    {
        "name": "THE FULLY ELECTRIC BMW i7",
        "image": "artifact/images\pexels-framesbyambro-14850149.jpg",
        "fuel": "Full-Electric",
        "price": "₹ 2,05,00,000",
        "new": False
    },
    {
        "name": "THE FIRST-EVER BMW i7 M70 xDRIVE",
        "image": "artifact/images\pexels-saimon-8253060.jpg",
        "fuel": "Full-Electric",
        "price": "₹ 2,50,00,000",
        "new": False
    },
    {
        "name": "THE FIRST-EVER BMW i5 M60 xDRIVE",
        "image": "artifact/images\P90505039_highRes_the-new-bmw-i5-m60-x.jpg",
        "fuel": "Full-Electric",
        "price": "₹ 1,19,50,000",
        "new": True
    }
]

# Display cards in rows of 3
for i in range(0, len(cars), 3):
    cols = st.columns(3)
    for idx, car in enumerate(cars[i:i+3]):
        with cols[idx]:
            st.image(car["image"], use_container_width=True)
            st.markdown(f"### {car['name']}")
            st.markdown(f"🔋 *{car['fuel']}*")
            st.markdown(f"**💰 Starting from {car['price']}**")
            if car["new"]:
                st.markdown("<span style='color: white; background-color: red; padding: 4px; border-radius: 4px;'>New</span>", unsafe_allow_html=True)
