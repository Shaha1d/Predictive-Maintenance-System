import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.set_page_config(page_title="Predictive Maintenance Dashboard", layout="wide")

st.title("Predictive Maintenance Dashboard")
st.write("This dashboard predicts the probability of machine failure based on real-time sensor data.")

model_path = "model.pkl" if os.path.exists("model.pkl") else "src/model.pkl"
data_path = "predictive_maintenance.csv" if os.path.exists("predictive_maintenance.csv") else "src/predictive_maintenance.csv"

if not os.path.exists(model_path):
    st.error(f"Model file not found at {model_path}. Please check your repository.")
else:
    try:
        model = joblib.load(model_path)
        st.success("Model loaded successfully!")
    except Exception as e:
        st.error(f"Error loading the model: {e}")

if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    st.subheader("Dataset Preview")
    st.dataframe(df.head())
else:
    st.info("Dataset file not found, but the model is ready if you want to add inputs.")
