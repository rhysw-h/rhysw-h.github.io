import pandas as pd

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_Russian_federal_subjects_by_GRDP"

# Use pandas to scrape the table directly from the URL
tables = pd.read_html(url)

# Since the GRDP table is the first one on the page, we can select the first table
grdp_df = tables[0]

# Display the DataFrame
print(grdp_df)

# Optionally, save it to a CSV file
grdp_df.to_csv("russian_grdp.csv", index=False)
