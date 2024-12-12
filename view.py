import pandas as pd

# Load joined data
joined_data_path = '/Users/ermaswartz/Documents/methods_data/joined_data.csv'
data = pd.read_csv(joined_data_path)

# Print columns to verify the presence of 'borough'
print("Columns in the dataset:", data.columns)

# Check unique values in 'borough' column if it exists
if 'borough' in data.columns:
    print("Unique values in 'borough':", data['borough'].unique())
else:
    print("The column 'borough' does not exist. Please verify the column names.")