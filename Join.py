import pandas as pd
import os

# Define file paths
main_data_path = '/Users/ermaswartz/Documents/methods_data/main_data.csv'
flood_index_path = '/Users/ermaswartz/Documents/methods_data/flood_index.csv'

# Load datasets
main_data = pd.read_csv(main_data_path)
flood_index = pd.read_csv(flood_index_path)

# Ensure the GEOID columns are of the same type for joining
main_data['GEOID'] = main_data['GEOID'].astype(str)
flood_index['GEOID'] = flood_index['GEOID'].astype(str)

# Perform the join on GEOID
joined_data = pd.merge(main_data, flood_index, on='GEOID', how='inner')

# Save the joined dataset to a new CSV
output_path = '/Users/ermaswartz/Documents/methods_data/joined_data.csv'
joined_data.to_csv(output_path, index=False)

print(f"Joined data saved to {output_path}")