import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_Russian_federal_subjects_by_GRDP"
tables = pd.read_html(url)
grdp_df = tables[0]
grdp_df.to_csv("russian_grdp.csv", index=False)
