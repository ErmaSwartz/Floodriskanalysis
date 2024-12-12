import pandas as pd

# File paths
pluto_with_ntas_path = "/Users/ermaswartz/Documents/methods_data/CSVs/pluto_with_ntas.csv"
output_path = "/Users/ermaswartz/Documents/methods_data/CSVs/pluto_reduced_by_ntacode_and_zoning.csv"

# Load PLUTO with NTAs data
print("Loading PLUTO with NTAs data...")
pluto_data = pd.read_csv(pluto_with_ntas_path, low_memory=False)

# Relevant columns for grouping and aggregation
grouping_columns = [
    "ntacode", "zonedist1", "zonedist2", "zonedist3", "zonedist4", 
    "overlay1", "overlay2", "spdist1", "spdist2", "spdist3", "ntaname"
]

summarization_columns = [
    "lotarea", "bldgarea", "unitsres", "unitstotal", 
    "assessland", "assesstot", "latitude", "longitude"
]

# Filter dataset dynamically for existing columns
print("Filtering relevant columns...")
existing_columns = [col for col in grouping_columns + summarization_columns if col in pluto_data.columns]
filtered_data = pluto_data[existing_columns]
print(f"Columns retained: {filtered_data.columns.tolist()}")

# Handle missing values and normalize grouping columns
print("Cleaning grouping columns...")
for col in grouping_columns:
    if col in filtered_data.columns:
        filtered_data[col] = filtered_data[col].fillna("UNKNOWN").str.strip().str.upper()

# Group by `ntacode` and zoning columns, and aggregate
print("Grouping data by ntacode, zoning, and nta names...")
grouped_data = filtered_data.groupby([col for col in grouping_columns if col in filtered_data.columns]).agg({
    "lotarea": "sum",
    "bldgarea": "sum",
    "unitsres": "sum",
    "unitstotal": "sum",
    "assessland": "sum",
    "assesstot": "sum",
    "latitude": "mean",
    "longitude": "mean"
}).reset_index()

# Save the reduced dataset
print(f"Saving reduced data to {output_path}...")
grouped_data.to_csv(output_path, index=False)

print("Process completed successfully!")