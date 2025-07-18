# app.py

import streamlit as st
import pandas as pd
import joblib

# Load the trained model and training feature columns
model = joblib.load('model.pkl')

st.title("Advertising")

st.write("Enter the details below to predict the likelihood of advertisement.")

tv = st.number_input("TV Budget ($)", min_value=0.0, value=100.0)
radio = st.number_input("Radio Budget ($)", min_value=0.0, value=50.0)
newspaper = st.number_input("Newspaper Budget ($)", min_value=0.0, value=30.0)

# When the Predict button is clicked
if st.button("Predict"):
    # Prepare input as DataFrame
    input_dict = {
        'TV': tv,
        'Radio': radio,
        'Newspaper': newspaper
    }

    input_df = pd.DataFrame([input_dict])

    # Reindex to match training columns (in case any columns are missing)
    feature_columns=['TV', 'Radio', 'Newspaper']  
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    # Make prediction
    prediction = model.predict(input_df)[0]

    # Show result
    st.success(f"📈 Predicted Sales: {prediction:.2f} units")