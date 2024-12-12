import pandas as pd

# File paths
pluto_path = "/Users/ermaswartz/Documents/methods_data/CSVs/pluto_reduced_by_ntacode_and_zoning.csv"
final_data_path = "/Users/ermaswartz/Documents/methods_data/CSVs/final_joined_data.csv"
output_path = "/Users/ermaswartz/Documents/methods_data/CSVs/plutoanddemographic.csv"

# Load datasets
print("Loading datasets...")
pluto_data = pd.read_csv(pluto_path)
final_data = pd.read_csv(final_data_path)

# Normalize codes
print("Normalizing NTA codes...")
pluto_data['ntacode'] = pluto_data['ntacode'].fillna("UNKNOWN").str.strip().str.upper()
final_data['NTA2020'] = final_data['NTA2020'].fillna("UNKNOWN").str.strip().str.upper()

# Analyze distinct codes
pluto_ntas = set(pluto_data['ntacode'])
final_ntas = set(final_data['NTA2020'])

print(f"Unique NTAs in PLUTO: {len(pluto_ntas)}")
print(f"Unique NTAs in Final Data: {len(final_ntas)}")

# Check differences
only_in_pluto = pluto_ntas - final_ntas
only_in_final = final_ntas - pluto_ntas

print(f"NTAs only in PLUTO: {len(only_in_pluto)}")
print(f"NTAs only in Final Data: {len(only_in_final)}")

# Simplify Final Data codes to match PLUTO format
print("Simplifying Final Data codes...")
final_data['simplified_NTA'] = final_data['NTA2020'].str.extract(r'([A-Z]{2}\d{2})')  # Keep only the prefix

# Check simplified codes
simplified_final_ntas = set(final_data['simplified_NTA'].dropna())

# Compare again
print(f"Unique simplified NTAs in Final Data: {len(simplified_final_ntas)}")
remaining_only_in_pluto = pluto_ntas - simplified_final_ntas
remaining_only_in_final = simplified_final_ntas - pluto_ntas

print(f"Unmatched NTAs in PLUTO after simplification: {len(remaining_only_in_pluto)}")
print(f"Unmatched NTAs in Final Data after simplification: {len(remaining_only_in_final)}")

# Perform the join using the simplified NTA column
print("Attempting join with simplified codes...")
merged_data = pd.merge(
    pluto_data, 
    final_data, 
    left_on='ntacode', 
    right_on='simplified_NTA', 
    how='inner'
)

# Validate results
print(f"Merged data has {merged_data.shape[0]} rows and {merged_data.shape[1]} columns.")

# Save the merged dataset
print(f"Saving merged data to {output_path}...")
merged_data.to_csv(output_path, index=False)

print("Process completed successfully!")