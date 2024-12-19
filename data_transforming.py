# Import Libraries
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Today's Date
today = datetime.today()

# Save to CSV with today's date
filename = f"data_ingested/ETH_USD_{today.strftime('%Y-%m-%d')}.csv"

# Import Testing Data
test_data = pd.read_csv(filename)

# Find the Close Difference
test_diff = test_data['Close'].diff().dropna()

# Prepare sequences
def create_sequences(data, look_back=5):
    X, y = [], []
    for i in range(len(data) - look_back):
        X.append(data[i:(i + look_back)])
        y.append(data[i + look_back])
    return np.array(X), np.array(y)

# Set 5 days to look back into
look_back = 5

# Get teh Numpy arrays
X2, y2 = create_sequences(test_diff, look_back=look_back)

# Get the last 5 'Close_Diff' values
last_5_diff = test_data['Close'].diff().dropna()

# Reshape to 5x1
last_5_diff_values = last_5_diff.values.reshape(1, 5)

# Save model input
np.save(f"data_transformed/last_5_close_diff_{today.strftime('%Y-%m-%d')}.npy", last_5_diff_values)
