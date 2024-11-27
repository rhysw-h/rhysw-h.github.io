import pandas as pd

# Load dataset
data_url = "national_team_appearances.csv"
df = pd.read_csv(data_url)

# Create ppg by dividing 'Pts' by 'Pld'
df['ppg'] = df['Pts'] / df['Pld']

# Select only relevant columns
tidy_data = df[['Team', 'Part', 'ppg']]

# Save the tidy data to a CSV file
tidy_data.to_csv("ppg of participants.csv", index=False)
