import pandas as pd
import requests

# Load GRDP data
grdp_url = "https://raw.githubusercontent.com/rhysw-h/rhysw-h.github.io/refs/heads/main/updated_russian_grdp.csv"
grdp_df = pd.read_html(grdp_url)[0]

# Load GeoJSON data
geojson_url = "https://raw.githubusercontent.com/rhysw-h/rhysw-h.github.io/main/ru.geojson"
geojson_data = requests.get(geojson_url).json()

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
