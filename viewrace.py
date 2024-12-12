import pandas as pd

# File path
file_path = '/Users/ermaswartz/Documents/methods_data/census2020_race.csv'

# Load dataset
data = pd.read_csv(file_path, low_memory=False)

# Print column names
print("Column names:", data.columns)