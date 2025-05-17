import pandas as pd
import os

water_path = "data/clean_school_water_data.csv"
gdp_path = "data/clean_gdp_data.csv"
output_path = "data/merged_water_gdp.csv"

water_df = pd.read_csv(water_path)
gdp_df = pd.read_csv(gdp_path)

water_df['Country'] = water_df['Country'].str.strip()
gdp_df['Country'] = gdp_df['Country'].str.strip()

merged_df = pd.merge(water_df, gdp_df, on='Country', how='inner')

os.makedirs("data", exist_ok=True)
merged_df.to_csv(output_path, index=False)

print("Merged data saved to:", output_path)
print(merged_df.head())
