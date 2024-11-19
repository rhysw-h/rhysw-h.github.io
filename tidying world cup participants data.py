import pandas as pd

# Load the dataset
data_url = "national_team_appearances.csv"
df = pd.read_csv(data_url)

# Create the 'ppg' column by dividing 'Pts' by 'Pld'
df['ppg'] = df['Pts'] / df['Pld']

# Select only relevant columns: 'Team', 'Part', and 'ppg'
tidy_data = df[['Team', 'Part', 'ppg']]

# Save the tidy data to a CSV file
tidy_data.to_csv("ppg of participants.csv", index=False)

# Print the tidy data to check
print(tidy_data.head())
