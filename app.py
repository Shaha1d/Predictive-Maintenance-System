import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

class CustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if name == 'Model':
            class Model: pass
            return Model
        return super().find_class(module, name)

st.set_page_config(page_title="Predictive Maintenance Dashboard", layout="wide")

st.title("Predictive Maintenance Dashboard")
st.write("This dashboard predicts the probability of machine failure based on real-time sensor data.")

model_path = "model.pkl" if os.path.exists("model.pkl") else "src/model.pkl"

if not os.path.exists(model_path):
    st.error(f"Model file not found at {model_path}. Please check your repository.")
else:
    try:
        with open(model_path, 'rb') as f:
            model = CustomUnpickler(f).load()
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        model = None

    if model is not None:
        st.subheader("Current Sensor Status")
        
        data = {
            'Air_temperature': [298],
            'Process_temperature': [308],
            'Rotational_speed': [1500],
            'Torque': [40],
            'Tool_wear': [50]
        }
        df = pd.DataFrame(data)
        st.dataframe(df)
        
        st.sidebar.header("Input Sensor Features")
        air_temp = st.sidebar.slider("Air Temperature (K)", 295, 305, 298)
        proc_temp = st.sidebar.slider("Process Temperature (K)", 305, 315, 308)
        rot_speed = st.sidebar.slider("Rotational Speed (rpm)", 1100, 2800, 1500)
        torque = st.sidebar.slider("Torque (Nm)", 3, 76, 40)
        tool_wear = st.sidebar.slider("Tool Wear (min)", 0, 250, 50)
        
        input_data = pd.DataFrame([[air_temp, proc_temp, rot_speed, torque, tool_wear]], 
                                  columns=['Air_temperature', 'Process_temperature', 'Rotational_speed', 'Torque', 'Tool_wear'])
        
        if st.button("Predict Failure Status"):
            prediction = model.predict(input_data)
            if prediction[0] == 1:
                st.error("Warning: High probability of machine failure! Maintenance required.")
            else:
                st.success("Machine status is normal. No failure predicted.")
