import pandas as pd
import os

# File paths
final_joined_data_path = "/Users/ermaswartz/Documents/methods_data/csvs/final_joined_data.csv"
pluto_data_path = "/Users/ermaswartz/Documents/methods_data/CSVs/pluto_with_ntas.csv"
output_path = "/Users/ermaswartz/Documents/methods_data/csvs/filtered_merged_data.csv"

# Check if files exist
if not os.path.exists(final_joined_data_path):
    print(f"Error: File not found - {final_joined_data_path}")
    exit()

if not os.path.exists(pluto_data_path):
    print(f"Error: File not found - {pluto_data_path}")
    exit()

# Load datasets
try:
    print("Loading datasets...")
    final_joined_data = pd.read_csv(final_joined_data_path, low_memory=False)
    pluto_data = pd.read_csv(pluto_data_path, low_memory=False)
except Exception as e:
    print(f"Error reading the CSV files: {e}")
    exit()

# Normalize and clean NTA join columns
try:
    print("Normalizing NTA columns...")
    final_joined_data['NTA2020'] = final_joined_data['NTA2020'].astype(str).str.strip().str.upper()
    pluto_data['ntacode'] = pluto_data['ntacode'].astype(str).str.strip().str.upper()
except Exception as e:
    print(f"Error normalizing NTA columns: {e}")
    exit()

# Filter pluto_with_ntas based on matching NTAs in final_joined_data
try:
    print("Filtering pluto_with_ntas for matching NTAs...")
    matching_ntas = set(final_joined_data['NTA2020'])
    filtered_pluto_data = pluto_data[pluto_data['ntacode'].isin(matching_ntas)]
    print(f"Filtered pluto_with_ntas has {len(filtered_pluto_data)} rows.")
except Exception as e:
    print(f"Error filtering pluto_with_ntas: {e}")
    exit()

# Perform the join
try:
    print("Performing the join on NTA columns...")
    merged_data = pd.merge(final_joined_data, filtered_pluto_data, left_on='NTA2020', right_on='ntacode', how='inner')
    if merged_data.empty:
        print("Warning: The merged dataset is empty. Check the values in the NTA columns.")
    else:
        print(f"Merged data has {len(merged_data)} rows.")
except Exception as e:
    print(f"Error during merge: {e}")
    exit()

# Save the merged data
try:
    print(f"Saving merged data to {output_path}...")
    merged_data.to_csv(output_path, index=False)
    print(f"Merged data saved to {output_path}")
except Exception as e:
    print(f"Error saving the merged data: {e}")