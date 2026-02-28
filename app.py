import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load("car_price_model.pkl")

st.title("🚗 Car Price Prediction App")

# User Inputs
name = st.text_input("Car Name (Example: Maruti Swift Dzire VDI)")
year = st.number_input("Year", min_value=1990, max_value=2025)
km_driven = st.number_input("Kilometers Driven", min_value=0)
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG"])
seller_type = st.selectbox("Seller Type", ["Individual", "Dealer", "Trustmark Dealer"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox(
    "Owner Type",
    ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner"]
)

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "name": [name],
        "year": [year],
        "km_driven": [km_driven],
        "fuel": [fuel],
        "seller_type": [seller_type],
        "transmission": [transmission],
        "owner": [owner]
    })

    prediction = model.predict(input_data)

    st.success(f"Estimated Selling Price: ₹ {int(prediction[0]):,}")