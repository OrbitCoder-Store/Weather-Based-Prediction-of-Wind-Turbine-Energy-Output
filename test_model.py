"""
Test script to validate the trained model's functionality.
Tests model predictions on sample data.
"""

import pandas as pd
import joblib
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error

# Load the trained model
model = joblib.load("power_prediction.sav")

# Load the dataset for testing
df = pd.read_csv("data/T1.csv")
df.columns = df.columns.str.strip()

# Features and target
X = df[['WindSpeed(m/s)', 'Theoretical_Power_Curve (KWh)']]
y = df['LV ActivePower (kW)']

# Make predictions on the full dataset
predictions = model.predict(X)

# Calculate metrics
mse = mean_squared_error(y, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y, predictions)

print("=" * 50)
print("MODEL TESTING RESULTS")
print("=" * 50)
print(f"R² Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MSE: {mse:.4f}")
print("=" * 50)

# Test with sample data
print("\nSAMPLE PREDICTIONS:")
print("-" * 50)

sample_data = pd.DataFrame([
    [5.0, 100.0],
    [10.0, 200.0],
    [15.0, 300.0],
], columns=['WindSpeed(m/s)', 'Theoretical_Power_Curve (KWh)'])

sample_predictions = model.predict(sample_data)

for idx, (ws, tp) in enumerate(zip(sample_data['WindSpeed(m/s)'], 
                                    sample_data['Theoretical_Power_Curve (KWh)'])):
    print(f"Test {idx + 1}:")
    print(f"  Wind Speed: {ws} m/s")
    print(f"  Theoretical Power: {tp} KWh")
    print(f"  Predicted Power: {sample_predictions[idx]:.2f} kW")
    print()

print("✅ Model test completed successfully!")
