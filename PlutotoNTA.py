import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# File paths
pluto_data_path = "/Users/ermaswartz/Documents/methods_data/CSVs/PLUTO/pluto_24v3_1.csv"
nta_shapefile_path = "/Users/ermaswartz/Documents/methods_data/NTAs/geo_export_387f4a6f-497b-44f9-863f-c19f95b8a2fa.shp"
output_path = "/Users/ermaswartz/Documents/methods_data/CSVs/PLUTO/pluto_with_ntas.csv"

# Load PLUTO data
print("Loading PLUTO data...")
pluto_data = pd.read_csv(pluto_data_path, low_memory=False)

# Check for latitude and longitude columns in PLUTO data
if 'latitude' not in pluto_data.columns or 'longitude' not in pluto_data.columns:
    print("Error: Latitude and Longitude columns are required in the PLUTO dataset.")
    exit()

# Convert PLUTO data to GeoDataFrame with Point geometries
print("Converting latitude and longitude to geometries...")
geometry = [Point(xy) for xy in zip(pluto_data['longitude'], pluto_data['latitude'])]
pluto_gdf = gpd.GeoDataFrame(pluto_data, geometry=geometry, crs="EPSG:4326")  # WGS 84

# Load NTA shapefile
print("Loading NTA shapefile...")
nta_boundaries = gpd.read_file(nta_shapefile_path)

# Ensure CRS matches between PLUTO data and NTA boundaries
print("Ensuring CRS alignment...")
nta_boundaries = nta_boundaries.to_crs(pluto_gdf.crs)

# Perform spatial join
print("Performing spatial join to assign NTAs...")
merged_gdf = gpd.sjoin(pluto_gdf, nta_boundaries, how="left", predicate="within")

# Save the result
print(f"Saving merged data with NTAs to {output_path}...")
merged_gdf.to_csv(output_path, index=False)

print("Process completed successfully!")