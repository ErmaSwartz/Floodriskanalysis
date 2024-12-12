import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
joined_data = pd.read_csv("joined_data.csv")
demographics_data = pd.read_csv("Demographics_by_NTA_Cleaned.csv")

# Ensure columns are strings for proper matching
joined_data["NTA2020"] = joined_data["NTA2020"].astype(str).str.strip()
demographics_data["NTA2020"] = demographics_data["NTA2020"].astype(str).str.strip()

# Merge datasets on NTA2020
merged_data = pd.merge(joined_data, demographics_data, on="NTA2020", how="inner")

# Filter for South Bronx neighborhoods
south_bronx_neighborhoods = [
    "Melrose", "Mott Haven-Port Morris", "Morrisania", "Hunts Point", "Longwood"
]
south_bronx_data = merged_data[merged_data["Neighborhood"].isin(south_bronx_neighborhoods)]

# Calculate average FSHRI score for each neighborhood
flood_risk_by_neighborhood = (
    south_bronx_data.groupby("Neighborhood")["FSHRI"]
    .mean()
    .reset_index()
    .rename(columns={"FSHRI": "AverageFloodRisk"})
)

# Merge flood risk with demographic data
flood_and_demographics = pd.merge(
    flood_risk_by_neighborhood,
    demographics_data,
    on="NTA2020",
    how="inner"
)

# Visualization: Stacked bar chart for flood risk by demographic groups in each neighborhood
for neighborhood in south_bronx_neighborhoods:
    neighborhood_data = flood_and_demographics[
        flood_and_demographics["Neighborhood"] == neighborhood
    ]

    # Prepare data for stacked bar chart
    demographic_columns = ["PopulationGroups"]  # Add other relevant demographic columns
    neighborhood_data = neighborhood_data.melt(
        id_vars=["Neighborhood", "AverageFloodRisk"], 
        value_vars=demographic_columns,
        var_name="DemographicGroup", 
        value_name="Population"
    )

    # Plot stacked bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(
        neighborhood_data["DemographicGroup"],
        neighborhood_data["Population"],
        label=f"Flood Risk: {neighborhood_data['AverageFloodRisk'].iloc[0]:.2f}"
    )
    plt.title(f"Flood Risk by Demographic Groups in {neighborhood}")
    plt.xlabel("Demographic Groups")
    plt.ylabel("Population")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Visualization: Stacked bar chart for flood risk by demographic groups across all neighborhoods
citywide_data = merged_data[merged_data["FSHRI"] > 0]  # Only neighborhoods with some flood risk

# Group by demographic information
citywide_summary = citywide_data.groupby("PopulationGroups")["FSHRI"].mean().reset_index()

# Plot
plt.figure(figsize=(12, 7))
plt.bar(citywide_summary["PopulationGroups"], citywide_summary["FSHRI"], color="skyblue")
plt.title("Flood Risk by Demographic Groups (Citywide)")
plt.xlabel("Demographic Groups")
plt.ylabel("Average Flood Risk")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()