import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/National_team_appearances_in_the_FIFA_World_Cup"

# Fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the table
tables = soup.find_all("table", {"class": "wikitable"})
target_table = None

for table in tables:
    if "Rank" in str(table):  # Look for keyword 'Rank' in the table headers
        target_table = table
        break


if target_table:
    rows = target_table.find_all("tr")
    data = []
    headers = [header.text.strip() for header in rows[0].find_all("th")]

    for row in rows[1:]:
        cols = row.find_all(["td", "th"])
        cols = [col.text.strip() for col in cols]
        data.append(cols)

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Clean up the Dataframe
    df.replace(r'\[.*?\]', '', regex=True, inplace=True)

    # Save to CSV
    df.to_csv("national_team_appearances.csv", index=False)

