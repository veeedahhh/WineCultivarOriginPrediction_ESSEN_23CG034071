import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model, scaler = joblib.load("model/wine_cultivar_model.pkl")

st.set_page_config(page_title="Wine Cultivar Predictor", layout="centered")

st.title("🍷 Wine Cultivar Origin Prediction System")
st.write("Enter the wine's chemical properties to predict its cultivar.")

# User Inputs
alcohol = st.number_input("Alcohol", min_value=0.0)
malic_acid = st.number_input("Malic Acid", min_value=0.0)
alcalinity_of_ash = st.number_input("Alcalinity of Ash", min_value=0.0)
total_phenols = st.number_input("Total Phenols", min_value=0.0)
flavanoids = st.number_input("Flavanoids", min_value=0.0)
proline = st.number_input("Proline", min_value=0.0)

if st.button("Predict Cultivar"):
    input_data = np.array([[alcohol, malic_acid, alcalinity_of_ash,
                            total_phenols, flavanoids, proline]])

    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]

    st.success(f"Predicted Wine Cultivar: **Cultivar {prediction + 1}**")
