import requests
import streamlit as st
import json


st.title("L'application du Fleuriste 🌷")


features = {
    "sepal_length" : st.slider("Sepal.Length", 0.0, 10.0, 0.1),
    "sepal_width" : st.slider("Sepal.Width", 0.0, 10.0, 0.1),
    "petal_length" : st.slider("Petal.Length", 0.0, 10.0, 0.1),
    "petal_width" : st.slider("Petal.Width", 0.0, 10.0, 0.1)
}

button_clicked = st.button("What is this flower?")

if button_clicked:
    prediction = requests.post('http://server:8000/predict', json=features)
    st.success(f"{prediction.json()}")
    st.snow()