import pandas as pd

input_path = "data/freshwater_per_capita_2021.csv"
output_path = "data/clean_freshwater_data.csv"

df = pd.read_csv(input_path, header=None, skiprows=1)

df.columns = [
    "Country", "Country Code", "Indicator Name", "Indicator Code",
    "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"
]

df_clean = df[['Country', '2021']].rename(columns={
    '2021': 'Freshwater Per Capita 2021'
})

df_clean = df_clean.dropna(subset=['Freshwater Per Capita 2021'])

exclude_keywords = [
    "income", "World", "countries", "Euro area", "Arab World",
    "Sub-Saharan", "OECD", "IDA", "IBRD", "Latin America", "Asia"
]
df_clean = df_clean[~df_clean['Country'].str.contains('|'.join(exclude_keywords), case=False)]

df_clean.to_csv(output_path, index=False)

print("Clean freshwater data saved to:", output_path)
