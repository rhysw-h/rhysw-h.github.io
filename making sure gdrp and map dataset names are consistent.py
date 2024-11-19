import pandas as pd
import requests

# Load GRDP data
grdp_url = "https://en.wikipedia.org/wiki/List_of_Russian_federal_subjects_by_GRDP"
grdp_df = pd.read_html(grdp_url)[0]

# Load GeoJSON data
geojson_url = "https://raw.githubusercontent.com/rhysw-h/rhysw-h.github.io/main/ru.geojson"
geojson_data = requests.get(geojson_url).json()

# Example mapping to fix inconsistencies between datasets
name_corrections = {
    "Moscow": "Moskva", 
    "Saint Petersburg": "City of St. Petersburg",
    "Krasnoyarsk": "Krasnoyarsk Krai",
    "Omsk": "Omsk Oblast",
    "Saratov": "Saratov Oblast",
    "Primor'ye": "Primorsky Krai",
    "Tyumen'": "Tyumen Oblast",
    "Kaliningrad": "Kaliningrad Oblast",
    "Khabarovsk": "Khabarovsk Krai",
    "Tula": "Tula Oblast",
    "Chita": "Zabaykalsky Krai",  # Chita was part of Zabaykalsky Krai
    "Bashkortostan": "Bashkortostan Republic",  # Add full name for clarity
    # Add more corrections as needed
}

# Apply corrections to GRDP dataset
grdp_df["Federal subject"] = grdp_df["Federal subject"].replace(name_corrections)

# Apply corrections to GeoJSON data
for feature in geojson_data['features']:
    region_name = feature["properties"]["name"]
    if region_name in name_corrections:
        feature["properties"]["name"] = name_corrections[region_name]


# Display regions that were not matched
missing_regions = [feature["properties"]["name"] for feature in geojson_data['features']
                   if feature["properties"].get("GRDP_billion_RUB") is None]

print("Missing regions:", missing_regions)
