import pandas as pd
import yfinance as yf

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
    
    # Fetch fundamental data
    stock_info = stock_symbol.info
    stock_data['sector'] = stock_info.get('sector', 'N/A')
    stock_data['industry'] = stock_info.get('industry', 'N/A')
    stock_data['market_cap'] = stock_info.get('marketCap', 'N/A')
    
    # Add to list
    all_data.append(stock_data)

# Combine all data into one DataFrame
combined_data = pd.concat(all_data, ignore_index=True)

last_7_days = combined_data.tail(7)

# Remove today's data from the dataset
past_data = combined_data.drop(index=last_7_days.index)

# Save past_data
past_data.to_csv("train_data.csv", index=False)

last_7_days.to_csv("test_data.csv", index=False)

print("train_data.csv and test_data.csv have been saved.")
