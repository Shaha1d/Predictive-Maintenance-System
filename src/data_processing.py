import pandas as pd
import numpy as np

def load_and_clean_data(file_path):
    """
    Load and clean sensor data for predictive maintenance.
    """
    print(f"Loading sensor dataset from: {file_path}...")
    
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
        
    # Drop rows with missing values to ensure data quality
    df = df.dropna()
    
    print(f"Data successfully loaded! Dataset shape: {df.shape}")
    return df

if _name_ == "_main_":
    sample_path = "data/predictive_maintenance.csv"
    print("Data processing script initialized successfully.")
