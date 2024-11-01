import pandas as pd
from datetime import datetime

# Load the data
df = pd.read_csv('cocacola stocks.csv')

# Convert the 'Date' column to datetime and then to ISO 8601 format
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

# Save the formatted data
df.to_csv('formatted_data.csv', index=False)
