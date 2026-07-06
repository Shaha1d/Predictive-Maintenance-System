# Predictive Maintenance System

A comprehensive Machine Learning and Data Science project designed to predict industrial equipment failures before they occur, minimizing downtime and optimizing maintenance schedules.

## Architecture and Components
- src/data_processing.py: Handles sensor data ingestion, clean-up, and missing value filtering.
- src/train_model.py: Trains a RandomForest Classifier on industrial sensor metrics to capture multi-variable degradation patterns.
- app.py: An interactive, production-ready dashboard built with Streamlit to simulate real-time sensor parameters and display instant predictive failure risks.

## Sensor Features Analyzed
- Air Temperature (K) and Process Temperature (K)
- Rotational Speed (rpm) and Torque (Nm)
- Tool Wear (min)

## How to Run Locally
1. Clone the repository.
2. Install dependencies: pip install -r requirements.txt
3. Train the model: python src/train_model.py
4. Launch the dashboard: streamlit run app.py
