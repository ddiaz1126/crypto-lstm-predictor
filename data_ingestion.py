import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Fetch 1 month of data
stock_symbol = yf.Ticker("ETH-USD")
stock_data = stock_symbol.history(period="1mo", interval='1d', actions=True)

# Filter the last 6 days
today = datetime.today()
six_days_ago = today - timedelta(days=6)
# Filter between six days ago and today
filtered_data = stock_data[(stock_data.index >= six_days_ago.strftime('%Y-%m-%d')) & 
                           (stock_data.index < today.strftime('%Y-%m-%d'))]
# Save to CSV with today's date
filename = f"data_ingested/ETH_USD_{today.strftime('%Y-%m-%d')}.csv"
filtered_data.to_csv(filename)

print(f"CSV saved as {filename}")