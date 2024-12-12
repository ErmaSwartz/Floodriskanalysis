import pandas as pd
from statsmodels.api import OLS, add_constant

File_path= '/Users/ermaswartz/Documents/methods_data/csvs/final_joined_data.csv' 

def regression_south_bronx(file_path):
    # Load the dataset
    try:
        final_data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    # Filter for South Bronx neighborhoods using the 'Neighborhood' column
    south_bronx_neighborhoods = [
        "Melrose", "Mott Haven-Port Morris", "Morrisania", 
        "Hunts Point", "Longwood"
    ]
    south_bronx_data = final_data[final_data['Neighborhood'].isin(south_bronx_neighborhoods)]

    # Ensure relevant columns are numeric
    south_bronx_data['FSHRI'] = pd.to_numeric(south_bronx_data['FSHRI'], errors='coerce')

    # Define racial demographic columns
    racial_columns = [
        'Estimate Total: White alone',
        'Estimate Total: Black or African American alone',
        'Estimate Total: American Indian and Alaska Native alone',
        'Estimate Total: Asian alone',
        'Estimate Total: Native Hawaiian and Other Pacific Islander alone',
        'Estimate Total: Some Other Race alone',
        'Estimate Total: Two or More Races:'
    ]

    # Aggregate by NTA2020
    aggregated_data = south_bronx_data.groupby('NTA2020').agg(
        mean_FSHRI=('FSHRI', 'mean'),
        **{col: (col, 'sum') for col in racial_columns},
        total_population=('Estimate Total:', 'sum')
    ).reset_index()

    # Normalize racial counts to proportions
    for col in racial_columns:
        aggregated_data[col + '_proportion'] = aggregated_data[col] / aggregated_data['total_population']

    # Prepare data for regression
    X = aggregated_data[[col + '_proportion' for col in racial_columns]]
    X = add_constant(X)  # Add constant for regression
    y = aggregated_data['mean_FSHRI']

    # Run regression
    model = OLS(y, X).fit()

    # Display regression results
    print(model.summary())

    # Find the racial group most at risk
    most_at_risk_group = (
        aggregated_data[[col + '_proportion' for col in racial_columns]].mean().idxmax()
    )
    print(f"\nThe racial group most at risk in the South Bronx is: {most_at_risk_group.replace('_proportion', '')}")

# Run the South Bronx-specific regression
file_path = '/Users/ermaswartz/Documents/methods_data/csvs/final_joined_data.csv'
regression_south_bronx(file_path)