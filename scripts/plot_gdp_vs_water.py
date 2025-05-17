import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

df = pd.read_csv("data/merged_water_gdp.csv")

df = df[df['GDP Per Capita in 2023'] > 100]

x = df['GDP Per Capita in 2023']
y = df['Pct Basic Water Access']

plt.figure(figsize=(10, 6))
plt.xscale('log')  
plt.scatter(x, y, alpha=0.8)

z = np.polyfit(np.log10(x), y, 1)
p = np.poly1d(z)
plt.plot(x, p(np.log10(x)), linestyle="--", label=f"Trendline: y = {z[0]:.2f}log(x) + {z[1]:.2f}")

for i, row in df.iterrows():
    if row['Pct Basic Water Access'] < 60 or row['GDP Per Capita in 2023'] > 50000:
        plt.annotate(row['Country'], (row['GDP Per Capita in 2023'], row['Pct Basic Water Access']),
                     textcoords="offset points", xytext=(4, 4), fontsize=8)

plt.title("GDP per Capita vs. Basic School Water Access (%)", fontsize=14)
plt.xlabel("GDP per Capita (USD, log scale)", fontsize=12)
plt.ylabel("Basic Water Access (%)", fontsize=12)
plt.ylim(0, 105)
plt.grid(True)
plt.legend()

os.makedirs("plots", exist_ok=True)
plt.tight_layout()
plt.savefig("plots/gdp_vs_water_access_log.png", dpi=300)
plt.show()
