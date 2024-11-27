import requests
import os

base_url = "https://api.worldbank.org/v2/country/PH/indicator/"

# where to save files
output_directory = "philippines_data/"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 9 indicators
indicator_codes = [
    "SP.POP.TOTL",  # Total population
    "SP.DYN.LE00.IN",  # Life expectancy at birth
    "NY.GDP.MKTP.CD",  # GDP
    "SL.UEM.TOTL.ZS",  # Unemployment
    "FP.CPI.TOTL",  # CPI
    "IT.NET.USER.ZS",  # Internet users
    "SH.DYN.MORT",  # Mortality rate
    "SP.URB.TOTL.IN.ZS",  # Urban population 
    "EG.FEC.RNEW.ZS"  # Renewable energy consumption
]

# Looping each indicator code
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
