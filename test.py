import pandas as pd

# Path to cleaned data
cleaned_path = '/Users/ermaswartz/Documents/methods_data/census_cleaned.csv'

# Load the dataset
cleaned_data = pd.read_csv(cleaned_path, low_memory=False)

# Print column names
print("Column names in cleaned data:", cleaned_data.columns)