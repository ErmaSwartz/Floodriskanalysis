import pandas as pd

# File paths
pluto_demo_path = "/Users/ermaswartz/Documents/methods_data/CSVs/plutoanddemographic.csv"
bronx_hispanic_path = "/Users/ermaswartz/Documents/methods_data/CSVs/Bronx_HispanicsOnlyData.csv"
output_path = "/Users/ermaswartz/Documents/methods_data/CSVs/final_combined_data.csv"

# Load datasets
print("Loading datasets...")
pluto_demo_data = pd.read_csv(pluto_demo_path, low_memory=False)
bronx_hispanic_data = pd.read_csv(bronx_hispanic_path, low_memory=False)

# Rename columns to match
print("Renaming columns for consistency...")
pluto_demo_data.rename(columns={'GEOID': 'GEO_ID'}, inplace=True)

# Normalize `GEO_ID` columns
print("Normalizing GEO_ID columns...")
pluto_demo_data['GEO_ID'] = pluto_demo_data['GEO_ID'].fillna("UNKNOWN").astype(str).str.strip().str.upper()
bronx_hispanic_data['GEO_ID'] = bronx_hispanic_data['GEO_ID'].fillna("UNKNOWN").astype(str).str.strip().str.upper()

# Perform the join
print("Joining datasets...")
merged_data = pd.merge(
    pluto_demo_data,
    bronx_hispanic_data,
    on='GEO_ID',
    how='inner'  # Adjust 'how' to 'left' or 'right' if needed
)

# Validate results
print(f"Merged data has {merged_data.shape[0]} rows and {merged_data.shape[1]} columns.")

# Save the merged dataset
print(f"Saving merged data to {output_path}...")
merged_data.to_csv(output_path, index=False)

print("Process completed successfully!")