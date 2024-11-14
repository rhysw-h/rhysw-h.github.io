import pandas as pd

url = "https://raw.githubusercontent.com/rhysw-h/rhysw-h.github.io/refs/heads/main/gdp%20growth%20rate%20countries%20over%20time.csv"
df = pd.read_csv(url)

# Change to long format using pd.melt()
long_df = pd.melt(
    df,
    id_vars=["Country Name"],
    var_name="Year",
    value_name="GDP Growth Rate"
)

long_df['Year'] = long_df['Year'].astype(int)
long_df.dropna(subset=['GDP Growth Rate'], inplace=True)

# Merge Japan and South Korea into one entry for the year 2002
long_df['Country Name'] = long_df.apply(
    lambda row: 'Japan & South Korea' if row['Country Name'] in ['Japan', 'South Korea'] and row['Year'] == 2002 
    else row['Country Name'], axis=1
)

# Define each country as host or winenr
wc_dict = {
    2002: {'Host': ['Japan & South Korea'], 'Winner': 'Brazil'},
    2006: {'Host': ['Germany'], 'Winner': 'Italy'},
    2010: {'Host': ['South Africa'], 'Winner': 'Spain'},
    2014: {'Host': ['Brazil'], 'Winner': 'Germany'},
    2018: {'Host': ['Russia'], 'Winner': 'France'},
    2022: {'Host': ['Qatar'], 'Winner': 'Argentina'}
}


filtered_rows = []


for year, info in wc_dict.items():
    # Get host and winner for the given year
    hosts = info['Host']
    winner = info['Winner']
    
    # Filter relevant rows for the host country
    for host in hosts:
        host_data = long_df[(long_df['Country Name'] == host) & 
                            (long_df['Year'].between(year - 2, year + 2))]
        host_data['Label'] = 'Host'
        host_data['Event Year'] = year
        filtered_rows.append(host_data)
    
    # Filter relevant rows for the winner country
    winner_data = long_df[(long_df['Country Name'] == winner) & 
                          (long_df['Year'].between(year - 2, year + 2))]
    winner_data['Label'] = 'Winner'
    winner_data['Event Year'] = year
    filtered_rows.append(winner_data)

filtered_df = pd.concat(filtered_rows)

# Create columns for T-2, T-1, T, T+1, T+2 (years relative to time of wc)
filtered_df['Relative Year'] = filtered_df['Year'] - filtered_df['Event Year']
pivot_df = filtered_df.pivot(index=['Country Name', 'Label', 'Event Year'], 
                             columns='Relative Year', 
                             values='GDP Growth Rate').reset_index()

# Rename the columns for clarity
pivot_df.rename(columns={-2: 'T-2', -1: 'T-1', 0: 'T', 1: 'T+1', 2: 'T+2'}, inplace=True)

# Save to a CSV file
pivot_df.to_csv("world_cup_gdp_analysis.csv", index=False)