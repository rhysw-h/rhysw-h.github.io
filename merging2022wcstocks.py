
import pandas as pd

# Load datasets
df_adidas = pd.read_csv('ADS.DE_stock_data.csv', skiprows=1)
df_hyundai = pd.read_csv('005380.KS_stock_data.csv', skiprows=1)
df_cola = pd.read_csv('KO_stock_data.csv', skiprows=1)
df_visa = pd.read_csv('V_stock_data.csv', skiprows=1)

# Rename columns
df_adidas.columns = ['Date', 'ADS.DE']
df_hyundai.columns = ['Date', '005380.KS']
df_cola.columns = ['Date', 'KO']
df_visa.columns = ['Date', 'V']

# Merge the datasets on the 'Date' column
merged_df = df_adidas.merge(df_hyundai, on='Date', how='outer')
merged_df = merged_df.merge(df_cola, on='Date', how='outer')
merged_df = merged_df.merge(df_visa, on='Date', how='outer')

# Sort by date
merged_df['Date'] = pd.to_datetime(merged_df['Date'])
merged_df = merged_df.sort_values('Date')

# Convert the date back to date format
merged_df['Date'] = merged_df['Date'].dt.strftime('%Y-%m-%d')

# Save to a CSV file with the new name
merged_df.to_csv('2022wcstocks.csv', index=False)

