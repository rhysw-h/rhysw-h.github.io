import pandas as pd

# Load the data
prices_df = pd.read_csv('https://eco-prices-scrapes.s3.eu-west-2.amazonaws.com/teaching/davies_price_data/db_prices.csv')
items_df = pd.read_csv('https://eco-prices-scrapes.s3.eu-west-2.amazonaws.com/teaching/davies_price_data/db_item_clean.csv')

# Merge prices with item descriptions
full_df = pd.merge(prices_df, items_df[['item_id', 'description']], on='item_id')

# Format the dates
full_df['quote_date'] = pd.to_datetime(full_df['quote_date'], format='%Y%m')

# Filter for chicken prices (modify "chicken" if needed)
chicken_df = full_df[full_df['description'].str.contains('chicken', case=False, na=False)]

# Extract year from dates
chicken_df['year'] = chicken_df['quote_date'].dt.year

# Map regions to ONS codes
region_codes = {
    2: "UKI",  # London
    3: "UKJ",  # South East
    4: "UKK",  # South West
    5: "UKH",  # East Anglia
    6: "UKF",  # East Midlands
    7: "UKG",  # West Midlands
    8: "UKE",  # Yorkshire & Humber
    9: "UKD",  # North West
    10: "UKC", # North
    11: "UKL", # Wales
    12: "UKM", # Scotland
    13: "UKN"  # Northern Ireland
}
chicken_df['region_code'] = chicken_df['region'].map(region_codes)

# Aggregate prices by year and region
agg_chicken_df = chicken_df.groupby(['year', 'region_code']).agg({'price': 'median'}).reset_index()

# Save the dataset as a CSV
agg_chicken_df.to_csv('chicken_prices_by_region_year.csv', index=False)

print("CSV file 'chicken_prices_by_region_year.csv' created!")
