import streamlit as st

st.header("BMW watches 𝑩𝑴𝑾☢⬜🟦🟥")
st.subheader("Welcome to my watches")
a = st.slider("pick a range",5000,1,30000)
st.write(f"The selected range is {a}")
#''st.selectbox('Select cars of your choice', options=['BMW M4','M5','M3','M2','M8','X7','X6'])''
st.image("artifact/images/bmw watch.jpg")
st.feedback(options="stars")
              
