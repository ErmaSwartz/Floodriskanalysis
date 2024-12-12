import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

# File path
data_path = "/Users/ermaswartz/Documents/methods_data/CSVs/plutoanddemographic.csv"

# Load the dataset
print("Loading data...")
data = pd.read_csv(data_path)

# Normalize zoning data
print("Normalizing zoning data...")
data['industrial'] = data['zonedist1'].str.startswith('M').astype(int)

# Aggregate by NTA
print("Aggregating by NTA...")
nta_analysis = data.groupby('ntacode').agg(
    industrial_proportion=('industrial', 'mean'),
    mean_flood_risk=('FSHRI', 'mean'),
    total_population=('Estimate Total:', 'sum'),
    **{col: (col, 'sum') for col in [
        'Estimate Total: White alone',
        'Estimate Total: Black or African American alone',
        'Estimate Total: Asian alone',
    ]}
).reset_index()

# Add racial proportions
racial_columns = [
    'Estimate Total: White alone',
    'Estimate Total: Black or African American alone',
    'Estimate Total: Asian alone'
]
for col in racial_columns:
    nta_analysis[col + '_proportion'] = nta_analysis[col] / nta_analysis['total_population']

# Separate data for the Bronx and the rest of the city
bronx_data = nta_analysis[nta_analysis['ntacode'].str.startswith('BX')]
rest_of_city_data = nta_analysis[~nta_analysis['ntacode'].str.startswith('BX')]

# Function to perform regressions
def perform_regressions(data, label):
    print(f"=== {label} Analysis ===")
    
    # Zoning and Race Regression
    print(f"Analyzing the relationship between zoning and race ({label})...")
    for race_col in racial_columns:
        print(f"Regression for industrial zoning vs. {race_col} ({label})...")
        X_race = data[['industrial_proportion']]
        X_race = sm.add_constant(X_race)
        y_race = data[race_col + '_proportion']
        race_model = sm.OLS(y_race, X_race).fit()
        print(race_model.summary())
    
    # Race and Flood Risk Regression
    print(f"Analyzing the relationship between race and flood risk ({label})...")
    for race_col in racial_columns:
        print(f"Regression for flood risk vs. {race_col} ({label})...")
        X_flood = data[[race_col + '_proportion']]
        X_flood = sm.add_constant(X_flood)
        y_flood = data['mean_flood_risk']
        flood_model = sm.OLS(y_flood, X_flood).fit()
        print(flood_model.summary())

    # Correlation Matrices
    print(f"Generating correlation matrix for {label}...")
    plt.figure(figsize=(12, 8))
    sns.heatmap(
        data[['industrial_proportion'] + [col + '_proportion' for col in racial_columns]].corr(),
        annot=True, cmap='coolwarm', fmt=".2f"
    )
    plt.title(f'Correlation Matrix: Zoning and Race ({label})')
    plt.tight_layout()
    plt.savefig(f'zoning_race_correlation_{label.lower().replace(" ", "_")}.png')
    plt.show()
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(
        data[['mean_flood_risk'] + [col + '_proportion' for col in racial_columns]].corr(),
        annot=True, cmap='coolwarm', fmt=".2f"
    )
    plt.title(f'Correlation Matrix: Race and Flood Risk ({label})')
    plt.tight_layout()
    plt.savefig(f'race_flood_correlation_{label.lower().replace(" ", "_")}.png')
    plt.show()

# Perform analysis for Bronx and Rest of NYC
perform_regressions(bronx_data, "Bronx")
perform_regressions(rest_of_city_data, "Rest of NYC (excluding Bronx)")