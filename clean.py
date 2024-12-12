import pandas as pd

# File paths
input_path = '/Users/ermaswartz/Documents/methods_data/Census.csv'
output_path = '/Users/ermaswartz/Documents/methods_data/census_cleaned.csv'

# Load the dataset
census_data = pd.read_csv(input_path, low_memory=False)

# Clean column names (remove whitespace and standardize)
census_data.columns = census_data.columns.str.strip()

# Filter rows where 'Borough' is 'Bronx'
if 'Borough' in census_data.columns:
    filtered_data = census_data[census_data['Borough'] == 'Bronx']
else:
    print("Error: 'Borough' column not found in the dataset.")
    exit()

# Save the filtered dataset to a new file
filtered_data.to_csv(output_path, index=False)

print(f"Filtered data saved to {output_path}")