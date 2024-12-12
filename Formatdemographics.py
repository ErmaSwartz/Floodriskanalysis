import re
import csv

# File paths
input_file = "/Users/ermaswartz/Documents/methods_data/CSVs/demoRAWcopypaste.csv"
output_file = "/Users/ermaswartz/Documents/methods_data/CSVs/parsed_demographics.csv"

# Function to clean and normalize rows
def clean_and_normalize_row(row):
    # Remove existing commas in numbers
    row_no_commas = re.sub(r"(\d),(\d)", r"\1\2", row)

    # Normalize spaces between fields
    normalized_row = re.sub(r"\s+", " ", row_no_commas).strip()

    return normalized_row

# Function to parse and structure cleaned rows (excluding `65+` columns)
def parse_row(row):
    # Regex to extract structured fields
    match = re.match(
        r"^(.+?)\s+([A-Z]{2}\d{2})\s+(\w+)\s+(\d+)\s+(\d+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)$",
        row,
    )
    if not match:
        return None  # Return None for rows that don't match the expected format

    # Extract matched groups into structured columns
    return [
        match.group(1),  # NTA Name
        match.group(2),  # NTA Code
        match.group(3),  # Borough Name
        match.group(4),  # Borough CD
        match.group(5),  # Total Population
        # Skipping columns related to `65+` information
        match.group(6),  # % Below Poverty
        match.group(7),  # % Hispanic/Latino
        match.group(8),  # % White
        match.group(9),  # % Black/African American
        match.group(10),  # % Asian
        match.group(11),  # % Other
    ]

# Process the file and save structured data
def process_and_save_file(input_path, output_path):
    with open(input_path, "r", encoding="ISO-8859-1") as file:  # Adjust encoding
        lines = file.readlines()

    cleaned_data = []
    for line in lines:
        cleaned_line = clean_and_normalize_row(line)
        parsed_row = parse_row(cleaned_line)
        if parsed_row:
            cleaned_data.append(parsed_row)

    # Save to a new CSV
    with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        # Write the header (excluding `65+` information)
        writer.writerow([
            "NTA Name", "NTA Code", "Borough Name", "Borough CD", "Total Population",
            "% Below Poverty", "% Hispanic/Latino", "% White",
            "% Black/African American", "% Asian", "% Other"
        ])
        # Write the cleaned data rows
        writer.writerows(cleaned_data)

# Run the processing
try:
    process_and_save_file(input_file, output_file)
    print(f"Processed data saved to: {output_file}")
except Exception as e:
    print(f"An error occurred: {e}")