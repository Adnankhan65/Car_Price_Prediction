import streamlit as st
import pickle
import pandas as pd
import numpy as np


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)


# -----------------------------
# Load Model
# -----------------------------

model = pickle.load(
    open("LinearRegressionModel.pkl", "rb")
)


# -----------------------------
# Load Dataset
# -----------------------------

car = pd.read_csv("Cleaned_Car_data.csv")


# -----------------------------
# Title
# -----------------------------

st.title("🚗 Car Price Prediction")

st.write(
    "Enter the car details to predict its estimated price."
)

st.divider()


# -----------------------------
# Get Values
# -----------------------------

companies = sorted(car["company"].unique())

car_models = sorted(car["name"].unique())

years = sorted(
    car["year"].unique(),
    reverse=True
)

fuel_types = sorted(
    car["fuel_type"].unique()
)


# -----------------------------
# Input Section
# -----------------------------

st.subheader("Enter Car Details")


company = st.selectbox(
    "Select Company",
    companies
)


car_model = st.selectbox(
    "Select Car Model",
    car_models
)


year = st.selectbox(
    "Select Year",
    years
)


fuel_type = st.selectbox(
    "Select Fuel Type",
    fuel_types
)


kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=10000,
    step=1000
)


# -----------------------------
# Prediction Button
# -----------------------------

if st.button(
    "Predict Car Price",
    use_container_width=True
):

    # Create DataFrame
    input_data = pd.DataFrame(
        {
            "name": [car_model],
            "company": [company],
            "year": [year],
            "kms_driven": [kms_driven],
            "fuel_type": [fuel_type]
        }
    )


    # Prediction
    prediction = model.predict(input_data)


    # Round prediction
    predicted_price = np.round(
        prediction[0],
        2
    )


    # -----------------------------
    # Display Prediction
    # -----------------------------

    st.success("Prediction completed!")

    st.metric(
        "Estimated Car Price",
        f"₹ {predicted_price:,.0f}"
    )