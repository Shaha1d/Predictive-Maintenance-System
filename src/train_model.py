import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_predictive_model(data_path, model_output_path):
    print("Loading data for training...")
    df = pd.read_csv(data_path)
    
    # Features (X) and Target (y)
    X = df[['Air_temperature', 'Process_temperature', 'Rotational_speed', 'Torque', 'Tool_wear']]
    y = df['Target']
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Initializing RandomForest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    print("Training the model...")
    model.fit(X_train, y_train)
    
    # Evaluate model performance
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    print(f"Model Training Complete! Accuracy: {acc * 100:.2f}%")
    print("\nClassification Report:\n", classification_report(y_test, predictions))
    
    # Save the trained model to a file
    joblib.dump(model, model_output_path)
    print(f"Model saved successfully at: {model_output_path}")

if _name_ == "_main_":
    train_predictive_model("data/predictive_maintenance.csv", "src/model.pkl")
