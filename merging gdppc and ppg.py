import pandas as pd

# Load datasets
gdppc_data = pd.read_csv("gdppc of countries 2024.csv")  # Replace with your GDPPC data file name
ppg_data = pd.read_csv("ppg of participants.csv")      # Replace with your World Cup participants data file name

# Rename columns for consistency
gdppc_data.rename(columns={'country': 'Team', 'gdppc': 'GDPPC'}, inplace=True)

# Normalize names in GDPPC dataset to match World Cup dataset
name_mapping = {
    "Bahamas, The": "Bahamas",
    "Brunei Darussalam": "Brunei",
    "Congo, Dem. Rep. of the": "DR Congo",
    "Congo, Republic of ": "Congo",
    "Côte d'Ivoire": "Ivory Coast",
    "China, People's Republic of": "China",
    "Korea, Republic of": "South Korea",
    "Micronesia, Fed. States of": "Micronesia",
    "Russian Federation": "Russia",
    "Slovak Republic": "Slovakia",
    "T rkiye, Republic of": "Turkey",
    "United States": "United States",
    "Venezuela, RB": "Venezuela"
    # Add more mappings as necessary
}

gdppc_data['Team'] = gdppc_data['Team'].replace(name_mapping)

# Filter out countries that never participated in the World Cup
world_cup_countries = ppg_data['Team'].unique()
gdppc_filtered = gdppc_data[gdppc_data['Team'].isin(world_cup_countries)]

# Merge the datasets
merged_data = ppg_data.merge(gdppc_filtered, on='Team', how='inner')

# Save the result to a CSV file
merged_data.to_csv("world_cup_gdppc_merged.csv", index=False)

# Print a preview of the resulting dataset
print(merged_data.head())