import requests
import os

# Base URL for the World Bank API
base_url = "https://api.worldbank.org/v2/country/PH/indicator/"

# Directory where files will be saved
output_directory = "philippines_data/"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# List of indicator codes to fetch
indicator_codes = [
    "SP.POP.TOTL",  # Total population
    "SP.DYN.LE00.IN",  # Life expectancy at birth
    "NY.GDP.MKTP.CD",  # GDP (current US$)
    "SL.UEM.TOTL.ZS",  # Unemployment, total (% of total labor force)
    "FP.CPI.TOTL",  # Consumer price index
    "SI.POV.DDAY",  # Poverty headcount ratio at $1.90 a day (2011 PPP)
    "NE.EXP.GOVT.ZS",  # Government expenditure on education, total (% of GDP)
    "IT.NET.USER.ZS",  # Internet users (per 100 people)
    "SH.DYN.MORT"  # Mortality rate, under-5 (per 1,000 live births)
]

# Loop through each indicator code to download data
for indicator in indicator_codes:
    api_url = f"{base_url}{indicator}?format=json"
    
    print(f"Attempting to download from: {api_url}")  # Print the URL for debugging
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:  # Check if the request was successful
            file_path = os.path.join(output_directory, f"{indicator}.json")
            
            with open(file_path, 'w') as json_file:
                json_file.write(response.text)
            print(f"Successfully downloaded {indicator}.json")
        else:
            print(f"Failed to download {indicator}: {response.status_code} - {response.text}")
    
    except Exception as e:
        print(f"Error downloading {indicator}: {e}")

print("Finished downloading data.")