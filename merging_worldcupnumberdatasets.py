import pandas as pd

# Load both datasets
sports_df = pd.read_csv('https://raw.githubusercontent.com/rhysw-h/rhysw-h.github.io/refs/heads/main/most-popular-sport-by-country-2024.csv')  # Dataset 1
location_df = pd.read_csv('https://raw.githubusercontent.com/rhysw-h/rhysw-h.github.io/refs/heads/main/longitude%20and%20latitude%20values_names1.csv')  # Dataset 2

# Merge datasets on the country column
merged_df = pd.merge(sports_df, location_df, how='left', left_on='Country', right_on='Country')

# Drop redundant columns and save to a new file if needed
merged_df = merged_df[['Country', 'mostpopularsport', 'Latitude (average)', 'Longitude (average)']]
merged_df.to_csv('merged_data.csv', index=False)

print(merged_df.head())
