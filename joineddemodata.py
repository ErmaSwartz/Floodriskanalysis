import pandas as pd

# File paths
bronx_demographics_path = "/Users/ermaswartz/Documents/methods_data/csvs/FINALDEMOGRAPHICS.csv"
joined_data_path = "/Users/ermaswartz/Documents/methods_data/csvs/joined_data.csv"
output_path = "/Users/ermaswartz/Documents/methods_data/csvs/final_joined_data.csv"

# Load the data
bronx_demographics = pd.read_csv(bronx_demographics_path)
joined_data = pd.read_csv(joined_data_path)

# Debug: Print column names to verify
print("Columns in Bronx Demographics Data before dropping 'Unnamed':")
print(bronx_demographics.columns)
print("Columns in Joined Data before dropping 'Unnamed':")
print(joined_data.columns)

# Drop columns containing "Unnamed" in both datasets
bronx_demographics = bronx_demographics.loc[:, ~bronx_demographics.columns.str.contains("Unnamed", case=False)]
joined_data = joined_data.loc[:, ~joined_data.columns.str.contains("Unnamed", case=False)]

# Debug: Print column names after dropping "Unnamed"
print("Columns in Bronx Demographics Data after dropping 'Unnamed':")
print(bronx_demographics.columns)
print("Columns in Joined Data after dropping 'Unnamed':")
print(joined_data.columns)

# Rename 'GEO_ID' to 'GEOID' in the Bronx demographics dataset to match the column in joined_data
bronx_demographics.rename(columns={"GEO_ID": "GEOID"}, inplace=True)

# Perform the join on the 'GEOID' column
try:
    final_data = pd.merge(joined_data, bronx_demographics, on="GEOID", how="inner")
    print(f"Joined data shape: {final_data.shape}")
    # Save the final joined data
    final_data.to_csv(output_path, index=False)
    print(f"Final joined data saved to {output_path}")
except KeyError as e:
    print(f"KeyError during join: {e}")
    print("Ensure column names in both datasets match exactly.")