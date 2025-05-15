import pandas as pd

input_path = "data/school_water_access_2024.xlsx"
output_path = "data/clean_school_water_data.csv"

df = pd.read_excel(input_path, sheet_name='Water Data')

df_clean = df[['name_WHO_EN', 'year', 'wat_bas_nat', 'wat_none_nat']].rename(columns={
    'name_WHO_EN': 'Country',
    'year': 'Year',
    'wat_bas_nat': 'Pct Basic Water Access',
    'wat_none_nat': 'Pct No Water Access'
})

df_clean = df_clean.dropna(subset=['Pct Basic Water Access', 'Pct No Water Access'])


df_clean = df_clean.sort_values('Year').groupby('Country').tail(1)

df_clean.to_csv(output_path, index = False)

print("Clean school water access data saved to:", output_path)

