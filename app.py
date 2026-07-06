
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Set page configuration
st.set_page_config(page_title="Predictive Maintenance System", layout="centered")

st.title("🏭 Predictive Maintenance Dashboard")
st.write("This dashboard predicts the probability of machine failure based on real-time sensor data.")

# Sidebar for user inputs (Sensors)
st.sidebar.header("⚙️ Machine Sensor Inputs")

air_temp = st.sidebar.slider("Air Temperature (K)", 295.0, 310.0, 298.0)
process_temp = st.sidebar.slider("Process Temperature (K)", 300.0, 315.0, 308.0)
rot_speed = st.sidebar.slider("Rotational Speed (rpm)", 1000, 3000, 1500)
torque = st.sidebar.slider("Torque (Nm)", 10.0, 80.0, 40.0)
tool_wear = st.sidebar.slider("Tool Wear (min)", 0, 250, 50)

# Create input dataframe
input_data = pd.DataFrame([{
    'Air_temperature': air_temp,
    'Process_temperature': process_temp,
    'Rotational_speed': rot_speed,
    'Torque': torque,
    'Tool_wear': tool_wear
}])

st.subheader("📊 Current Sensor Status")
st.dataframe(input_data)

# Check if model exists, if not show warning (since it trains locally)
model_path = "src/model.pkl"
if os.path.exists(model_path):
    # Load trained model
    import pickle
with open(model_path, 'rb') as f:
    model = pickle.load(f)
    
    # Predict
    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0][1]
    
    st.subheader("🔮 AI Prediction Results")
    if prediction == 1:
        st.error(f"🚨 Warning: High Risk of Machine Failure! (Probability: {prediction_proba*100:.1f}%)")
        st.write("⚠️ Recommendation: Schedule immediate preventive maintenance.")
    else:
        st.success(f"✅ Machine Status: Normal (Failure Probability: {prediction_proba*100:.1f}%)")
        st.write("👍 Current parameters are within safe operational limits.")
else:
    st.info("💡 Repository Setup Complete. Run 'src/train_model.py' locally to generate the model file (model.pkl) and enable active dashboard predictions.")
