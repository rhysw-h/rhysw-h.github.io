import pandas as pd
import numpy as np

# Load the merged dataset
df = pd.read_csv('2022wcstocks.csv')

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Filter for dates from November 1st, 2022 onwards
start_date = pd.to_datetime('2022-11-01')
df_filtered = df[df['Date'] >= start_date].copy()

# Get the first day's values for each stock
base_values = df_filtered[df_filtered['Date'] == start_date].iloc[0]

# Function to rebase a series
def rebase_series(series, base_value):
    return 100 * series / base_value

# Rebase each stock to 100
for column in df_filtered.columns:
    if column != 'Date':
        df_filtered[column] = rebase_series(df_filtered[column], base_values[column])

# Save the rebased data
df_filtered.to_csv('2022wcstocks_rebased.csv', index=False)

print("Data has been filtered, rebased, and saved to '2022wcstocks_rebased.csv'")

# Display the first few rows of the rebased data
print(df_filtered.head())