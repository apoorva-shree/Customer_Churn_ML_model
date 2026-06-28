# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:40:06 2026

@author: HP
"""

import streamlit as st
import pandas as pd
import pickle

# ---------------------------
# Load Model and Encoders
# ---------------------------

with open("customer_churn.pkl", "rb") as file:
    model_data = pickle.load(file)

with open("encoders.pkl", "rb") as file:
    encoders = pickle.load(file)

model = model_data["model"]
feature_names = model_data["feature_names"]

# ---------------------------
# Page Configuration
# ---------------------------

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction System")
st.write(
    "Enter customer details below and predict whether the customer is likely to churn."
)

st.divider()

# ---------------------------
# Input Section
# ---------------------------

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        encoders["gender"].classes_,
        index=None,
        placeholder="Select Gender"
    )

    SeniorCitizen = st.selectbox(
        "Senior Citizen",
        [0, 1],
        index=None,
        placeholder="Select Senior Citizen Status"
    )

    Partner = st.selectbox(
        "Partner",
        encoders["Partner"].classes_,
        index=None,
        placeholder="Select Partner Status"
    )

    Dependents = st.selectbox(
        "Dependents",
        encoders["Dependents"].classes_,
        index=None,
        placeholder="Select Dependents Status"
    )

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        value=None,
        placeholder="Enter Tenure"
    )

    PhoneService = st.selectbox(
        "Phone Service",
        encoders["PhoneService"].classes_,
        index=None,
        placeholder="Select Phone Service"
    )

    MultipleLines = st.selectbox(
        "Multiple Lines",
        encoders["MultipleLines"].classes_,
        index=None,
        placeholder="Select Multiple Lines Status"
    )

    InternetService = st.selectbox(
        "Internet Service",
        encoders["InternetService"].classes_,
        index=None,
        placeholder="Select Internet Service"
    )

    OnlineSecurity = st.selectbox(
        "Online Security",
        encoders["OnlineSecurity"].classes_,
        index=None,
        placeholder="Select Online Security Status"
    )

    OnlineBackup = st.selectbox(
        "Online Backup",
        encoders["OnlineBackup"].classes_,
        index=None,
        placeholder="Select Online Backup Status"
    )

with col2:

    DeviceProtection = st.selectbox(
        "Device Protection",
        encoders["DeviceProtection"].classes_,
        index=None,
        placeholder="Select Device Protection Status"
    )

    TechSupport = st.selectbox(
        "Tech Support",
        encoders["TechSupport"].classes_,
        index=None,
        placeholder="Select Tech Support Status"
    )

    StreamingTV = st.selectbox(
        "Streaming TV",
        encoders["StreamingTV"].classes_,
        index=None,
        placeholder="Select Streaming TV Status"
    )

    StreamingMovies = st.selectbox(
        "Streaming Movies",
        encoders["StreamingMovies"].classes_,
        index=None,
        placeholder="Select Streaming Movies Status"
    )

    Contract = st.selectbox(
        "Contract Type",
        encoders["Contract"].classes_,
        index=None,
        placeholder="Select Contract Type"
    )

    PaperlessBilling = st.selectbox(
        "Paperless Billing",
        encoders["PaperlessBilling"].classes_,
        index=None,
        placeholder="Select Paperless Billing Status"
    )

    PaymentMethod = st.selectbox(
        "Payment Method",
        encoders["PaymentMethod"].classes_,
        index=None,
        placeholder="Select Payment Method"
    )

    MonthlyCharges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=None,
        placeholder="Enter Monthly Charges"
    )

    TotalCharges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=None,
        placeholder="Enter Total Charges"
    )

# ---------------------------
# Prediction Button
# ---------------------------

if st.button("Predict Churn"):

    if None in [
        gender,
        SeniorCitizen,
        Partner,
        Dependents,
        tenure,
        PhoneService,
        MultipleLines,
        InternetService,
        OnlineSecurity,
        OnlineBackup,
        DeviceProtection,
        TechSupport,
        StreamingTV,
        StreamingMovies,
        Contract,
        PaperlessBilling,
        PaymentMethod,
        MonthlyCharges,
        TotalCharges
    ]:
        st.warning("Please fill all the fields before predicting.")
        st.stop()

    input_data = {
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }

    input_df = pd.DataFrame([input_data])

    # Apply saved encoders
    for column, encoder in encoders.items():
        input_df[column] = encoder.transform(
            input_df[column]
        )

    # Arrange columns exactly as model expects
    input_df = input_df[feature_names]

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.divider()
    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Customer is likely to churn.")
    else:
        st.success("✅ Customer is not likely to churn.")

    st.metric(
        label="Churn Probability",
        value=f"{probability:.2%}"
    )