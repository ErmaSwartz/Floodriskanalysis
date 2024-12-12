import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File path to the dataset
file_path = '/Users/ermaswartz/Documents/methods_data/flood_index.csv'

# Load the dataset
data = pd.read_csv(file_path, low_memory=False)
data.columns = data.columns.str.strip()  # Clean column names

# Define race categories and group combinations
races = [
    'White alone', 'Black or African American alone', 'Asian alone',
    'American Indian and Alaska Native alone', 'Some Other Race alone'
]
group_combinations = [
    'Population of one race', 'Population of two races', 'Population of three races',
    'Population of four races', 'Population of five races', 'Population of six races'
]

# Create output folder
output_folder = '/Users/ermaswartz/Documents/methods_data/charts/'
import os
os.makedirs(output_folder, exist_ok=True)

### Chart 1: Population by Race (Bar Chart)
plt.figure(figsize=(10, 6))
race_population = data[races].sum()
race_population.plot(kind='bar', color=['green', 'orange'], title='Population by Race')
plt.xlabel('Race')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_folder + 'population_by_race.png')
plt.show()

### Chart 2: Population by Racial Group Combinations (Stacked Bar Chart)
plt.figure(figsize=(10, 6))
group_data = data[group_combinations].sum()
group_data.plot(kind='bar', stacked=True, color=['green', 'orange'], title='Population by Racial Group Combinations')
plt.xlabel('Racial Group Combination')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_folder + 'population_by_group_combinations.png')
plt.show()

### Chart 3: Population Breakdown by Borough (Grouped Bar Chart)
if 'Borough' in data.columns:
    borough_data = data.groupby('Borough')[races].sum()
    borough_data.plot(kind='bar', figsize=(12, 6), color=['green', 'orange'], title='Population by Borough and Race')
    plt.xlabel('Borough')
    plt.ylabel('Population')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_folder + 'population_by_borough.png')
    plt.show()
else:
    print("Error: 'Borough' column not found in the dataset.")

### Chart 4: Racial Composition as a Proportion (Pie Chart)
plt.figure(figsize=(8, 8))
total_population = data['Total:'].sum()
proportions = (data[races].sum() / total_population) * 100
proportions.plot(kind='pie', colors=['green', 'orange'], autopct='%1.1f%%', title='Racial Composition Proportion')
plt.ylabel('')
plt.tight_layout()
plt.savefig(output_folder + 'racial_composition_proportion.png')
plt.show()

### Chart 5: Heatmap for Complex Racial Combinations
complex_combinations = [
    'White; Black or African American', 'White; Asian',
    'White; Native Hawaiian and Other Pacific Islander'
]
if set(complex_combinations).issubset(data.columns):
    plt.figure(figsize=(8, 6))
    heatmap_data = data[complex_combinations].sum().to_frame(name='Population')
    sns.heatmap(heatmap_data, annot=True, fmt="g", cmap=sns.color_palette("YlOrBr", as_cmap=True), cbar=False)
    plt.title('Population of Complex Racial Combinations')
    plt.tight_layout()
    plt.savefig(output_folder + 'complex_racial_combinations_heatmap.png')
    plt.show()
else:
    print("Error: Some complex combinations are missing in the dataset.")