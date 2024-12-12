# Floodriskanalysis

# Racial Zoning, Industrial Land Use, and Flood Risk Analysis in NYC

## Overview  
This project investigates the relationship between racially motivated zoning, heavy industrial activity, and contemporary climate-change-driven flood risks in the **South Bronx** and **New York City**. Using a robust quantitative methodology, the study highlights systemic inequities in flood risk exposure driven by historical zoning policies and environmental injustice.

## Objective  
The primary goal of this analysis is to:  
1. Evaluate how **racial demographics** influence flood risk exposure.  
2. Assess the role of **industrial zoning** in shaping flood vulnerability patterns.  
3. Highlight disparities at both the **South Bronx** and **city-wide** scales.  

By integrating flood risk data with demographic and land-use datasets, this project sheds light on environmental vulnerability and equity issues.

---

## Methodology  

### Data Sources  
- **Flood Risk Data**:  
  - Flood Hazard Surface Risk Index (FSHRI).  
  - Storm surge and tidal risk scores for current and future time horizons (2050s, 2080s).  
- **Demographic Data**:  
  - Neighborhood Tabulation Areas (NTA) data, including racial/ethnic composition, age distribution, and poverty indicators.  
- **Land Use Data**:  
  - NYC PLUTO dataset, providing zoning and industrial land-use information.  

### Analytical Approach  
1. **Data Cleaning**:  
   - Removal of duplicates and irrelevant columns.  
   - Harmonization of NTA identifiers and standardization of zoning data.  

2. **Data Integration**:  
   - Merging flood risk scores with demographic proportions at the neighborhood level.  
   - Normalizing industrial zones into binary variables based on zoning code.  

3. **Statistical Analysis**:  
   - Multiple Linear Regression to test relationships between racial proportions and flood risk scores.  
   - Comparative analysis of the South Bronx vs. the rest of NYC.  

4. **Visual Analysis**:  
   - Stacked bar charts for racial flood risk exposure.  
   - Correlation heatmaps for zoning, demographics, and flood risk relationships.  

---

## Key Findings  
1. **White Populations**: Negative correlation with flood risk (coefficient: -1.0644, p = 0.003).  
2. **Asian and Other Race Populations**: Significant positive correlation with flood risk.  
3. **Black/African American Populations**: Insignificant relationship, possibly due to heterogeneous spatial distribution.  
4. **Industrial Zoning**: Strong association with higher flood risk in marginalized neighborhoods.  

The findings underscore systemic inequities in zoning and flood vulnerability, particularly in historically underserved areas like the South Bronx.

---

## Repository Contents  

### Files  
- `methodology_analysis.py`: Python script for data cleaning, integration, regression modeling, and visual analysis.  
- `data/`: Directory containing placeholder datasets (ensure appropriate licensing and permissions for use).  
- `results/`: Outputs such as regression summaries, charts, and correlation matrices.  
- `quantitative_methodology_findings.docx`: Detailed explanation of the study, regression results, and key findings.  

### Code Summary  
The Python script performs the following steps:  
1. **Data Loading and Cleaning**  
2. **Normalization of Industrial Zoning Data**  
3. **Aggregation by Neighborhood (NTA)**  
4. **Multiple Linear Regressions** to test relationships between zoning, racial demographics, and flood risk.  
5. **Correlation Matrices** and visualizations to illustrate systemic trends.  

---

## How to Run  

### Prerequisites  
- Python 3.x  
- Required Libraries:  
   ```bash
   pip install pandas matplotlib seaborn statsmodels
   ```

### Instructions  
1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/racial-zoning-flood-risk.git
   cd racial-zoning-flood-risk
   ```

2. Place your cleaned data files in the `data/` folder.  

3. Run the script:  
   ```bash
   python methodology_analysis.py
   ```

4. Outputs (regression summaries, charts, and heatmaps) will be saved in the `results/` folder.

---

## Visualization Samples  
Example outputs include:  
- **Stacked Bar Charts**: Flood risk exposure by racial groups within neighborhoods.  
- **Heatmaps**: Correlations between industrial zoning, flood risk, and demographic proportions.  

---

## License  
This repository is released under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments  
This work draws on publicly available datasets from:  
- NYC Open Data  
- NYC Department of City Planning  
- FEMA Flood Hazard Data  

Special thanks to collaborators and reviewers for their invaluable feedback.


