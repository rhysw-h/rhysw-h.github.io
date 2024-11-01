import yfinance as yf
import pandas as pd
from datetime import datetime

# List of stock symbols
symbols = ['V', 'KO', 'ADS.DE', '005380.KS']

# Date range
start_date = '2019-11-01'
end_date = '2024-11-01'

for symbol in symbols:
    # Download the data
    data = yf.download(symbol, start=start_date, end=end_date)
    
    # Reset index to make Date a column
    data = data.reset_index()
    
    # Select only 'Date' and 'Close' columns
    data = data[['Date', 'Close']]
    
    # Convert Date to string in YYYY-MM-DD format
    data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')
    
    # Save to CSV
    filename = f"{symbol}_stock_data.csv"
    data.to_csv(filename, index=False)
    print(f"Data for {symbol} has been saved to {filename}")
