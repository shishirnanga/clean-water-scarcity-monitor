# 🌍 Clean Water Scarcity Monitor

An interactive data & analytics project exploring **global disparities in access to clean water**.  
This project builds ETL pipelines to process datasets (school water access, freshwater resources, GDP) and creates visualizations to uncover correlations between **socioeconomic factors and water availability**.

---

## ✨ Features
- **ETL Pipelines:** Scripts to clean and merge raw data into structured CSVs.
- **Data Sources:** WHO, UNICEF, UN, World Bank datasets.
- **Exploratory Analysis:** Identify patterns between GDP, governance, and water access.
- **Visualizations:** Charts showing geographic and economic disparities in clean water availability.
- **Reproducible:** Modular scripts (`scripts/etl_*.py`) to re-run the pipeline end-to-end.

---

## 📂 Project Structure
```
clean_water_project/
│── data/               # Raw + cleaned datasets
│── plots/              # Generated charts
│── scripts/            # ETL + analysis scripts
│   ├── etl_clean_water.py
│   ├── etl_freshwater.py
│   ├── etl_gdp.py
│   ├── etl_merge.py
│   └── plot_gdp_vs_water.py
│── requirements.txt    # Dependencies
│── README.md           # Project overview
```

---

## 🛠️ Tech Stack
- **Languages:** Python (pandas, matplotlib, seaborn, numpy)
- **ETL:** Pandas data pipelines (`read_excel`, `read_csv`, merging, cleaning)
- **Visualization:** Matplotlib + Seaborn charts
- **Data Sources:** WHO, UNICEF, World Bank (GDP, freshwater)

---

## 🚀 Getting Started

1. **Clone the repo:**
   ```bash
   git clone https://github.com/shishirnanga/clean-water-scarcity-monitor.git
   cd clean-water-scarcity-monitor
   ```

2. **Set up virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run ETL scripts:**
   ```bash
   python scripts/etl_clean_water.py
   python scripts/etl_freshwater.py
   python scripts/etl_gdp.py
   python scripts/etl_merge.py
   ```

4. **Generate plots:**
   ```bash
   python scripts/plot_gdp_vs_water.py
   ```

---

## 📊 Example Output

*(Insert chart images from your `plots/` folder)*  
```markdown
![GDP vs Water Access](plots/gdp_vs_water_access.png)
```

---

## 📈 Key Insights
- Countries with **low GDP but effective governance** still maintain good water access.  
- High GDP ≠ universal water access → infrastructure and policy are key.  
- Regions at risk can be identified for targeted aid and interventions.

---

## 🧭 Next Steps
- Add climate indicators (rainfall, drought frequency).  
- Deploy interactive dashboard with Streamlit or Tableau.  
- Expand analysis to **predict scarcity hotspots**.

---

## 👤 Author
**Shishir Nanga**  
- [LinkedIn](https://www.linkedin.com/in/shishir-nanga)  
- [GitHub](https://github.com/shishirnanga)  
