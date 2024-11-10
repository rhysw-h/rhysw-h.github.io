import json
import os
import glob

# Directory containing your JSON files
input_directory = "philippines_data/"  # Change this to your directory
output_file = "merged_philippines_data.json"

# Create an empty list to hold all data
merged_data = []

# Get all JSON files in the specified directory
json_files = glob.glob(os.path.join(input_directory, "*.json"))

# Loop through each JSON file and read its content
for json_file in json_files:
    with open(json_file, 'r') as f:
        # Load the JSON data from the file
        data = json.load(f)
        
        # Assuming each file has a list of records under a common key like 'data' or similar
        # If your structure is different, adjust this line accordingly
        merged_data.extend(data)  # Combine the lists

# Write the merged data to a new JSON file
with open(output_file, 'w') as f:
    json.dump(merged_data, f, indent=4)

print(f"Merged {len(json_files)} files into {output_file}.")
