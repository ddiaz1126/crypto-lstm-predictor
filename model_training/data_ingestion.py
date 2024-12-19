import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# List of Symbols for the Stocks
stock_list = [
    'ETH-USD',  # Ethereum
]

# Create an empty list to hold dataframes
all_data = []
for stock in stock_list:
    stock_symbol = yf.Ticker(stock)
    stock_data = stock_symbol.history(period="1y", interval='1d', actions=True)
    stock_data.reset_index(inplace=True)
    stock_data['stock_name'] = stock
    
    # Add to list
    all_data.append(stock_data)

# Combine all data into one DataFrame
combined_data = pd.concat(all_data, ignore_index=True)

# Get the last 6 days
today = datetime.today()
six_days_ago = today - timedelta(days=6)
last_6_days = combined_data[combined_data['Date'] >= six_days_ago.strftime('%Y-%m-%d')]

# Remove today's data from the dataset
past_data = combined_data.drop(index=last_6_days.index)

# Save past_data
past_data.to_csv("model_training/train_data.csv", index=False)

last_6_days.to_csv("model_training/test_data.csv", index=False)

print("train_data.csv and test_data.csv have been saved.")
