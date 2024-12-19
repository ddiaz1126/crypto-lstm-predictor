import pickle
import numpy as np
from datetime import datetime

# Today's Date
today = datetime.today()

# Save to CSV with today's date
filename = f"data_transformed/last_5_close_diff_{today.strftime('%Y-%m-%d')}.npy"

# Import Testing Data
last_5_diff_values = np.load(filename)

# Import Pipeline (MinMax Scalar and LSTM Model)
with open('model_pipeline.pkl', 'rb') as file:
    model_pipeline = pickle.load(file)

# Scale features
X_test_scaled = model_pipeline['X_scaler'].transform(last_5_diff_values)

#Make predictions using the LSTM model
predicted_diff_scaled = model_pipeline['model'].predict(X_test_scaled)

# Inverse transform to get back to the original scale
predicted_diff = model_pipeline['scaler_y'].inverse_transform(predicted_diff_scaled)

# Display the predicted differences
print(predicted_diff)

# Save model input
np.save(f"modeling_predictions/predicted_close_diff_{today.strftime('%Y-%m-%d')}.npy", predicted_diff)