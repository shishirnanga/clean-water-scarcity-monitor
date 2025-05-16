import pandas as pd
import os

input_path = "data/gdp_dataset.csv"
output_path = "data/clean_gdp_data.csv"

df = pd.read_csv(input_path, skiprows=4)

df_clean = df[['Country Name', '2023']].rename(columns={
    'Country Name': 'Country',
    '2023': 'GDP Per Capita in 2023'
})

df_clean = df_clean.dropna(subset=['GDP Per Capita in 2023'])

exclude_keywords = [
    "income", "World", "countries", "Euro area", "Arab World",
    "Sub-Saharan", "OECD", "IDA", "IBRD", "Latin America", "Asia"
]
df_clean = df_clean[~df_clean['Country'].str.contains('|'.join(exclude_keywords), case=False)]

df_clean['Country'] = df_clean['Country'].str.strip()

df_clean['GDP Per Capita in 2023'] = pd.to_numeric(df_clean['GDP Per Capita in 2023'], errors='coerce')

df_clean = df_clean.dropna()

os.makedirs("data", exist_ok=True)
df_clean.to_csv(output_path, index=False)

print("Clean GDP data saved to:", output_path)
