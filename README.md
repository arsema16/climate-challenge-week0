# 🌍 African Climate Trend Analysis (2015–2026)
**Path to COP32 | Prepared for Ethiopia's Ministry of Environment**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg)](https://climate-challenge-week0-1.streamlit.app/)

## 📋 Project Overview
This repository conducts an Exploratory Data Analysis (EDA) and Statistical Analysis of historical climate patterns across five key African nations: **Ethiopia, Kenya, Sudan, Tanzania, and Nigeria**. This data serves as the technical foundation for Ethiopia's strategic positioning at **COP32**.

## 🚀 Live Dashboard
The analysis has been deployed as an interactive dashboard for policy makers.
**View the Live App here:** [https://climate-challenge-week0-1.streamlit.app/](https://climate-challenge-week0-1.streamlit.app/)

## 🔍 Key Findings (Week 0)
* **Heat Stress:** Sudan exhibits the highest frequency of extreme heat days (> 35°C), signaling a need for urgent urban cooling infrastructure.
* **Statistical Significance:** A **One-Way ANOVA** was conducted across regional precipitation levels, resulting in a **p-value < 0.001**, statistically confirming significant climate variations between the studied regions.
* **Agricultural Risk:** High precipitation volatility was identified in the Ethiopian Highlands, suggesting a requirement for enhanced irrigation and water management investment.

## 📂 Folder Structure
```text
├── app/
│   └── main.py          # Streamlit Dashboard application
├── data/
│   └── all_countries_master.csv  # Final cleaned & merged dataset
├── notebooks/
│   └── compare_countries.ipynb   # Task 3: Statistical Analysis & ANOVA
├── scripts/
│   └── clean_all_countries.py          # Data pipeline and preprocessing
├── requirements.txt     # Production-ready dependencies
└── README.md            # Project documentation
## 🛠️ Setup & Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/arsema16/climate-challenge-week0.git](https://github.com/arsema16/climate-challenge-week0.git)
   cd climate-challenge-week0
   python -m venv venv

Set up Virtual Environment:

Bash
python -m venv venv

# Activate on Windows:
.\venv\Scripts\activate

# Activate on Linux/Mac:
source venv/bin/activate
Install Dependencies:

Bash
pip install -r requirements.txt
🧪 Technologies Used
Python 3.10+

Pandas & NumPy: Data Manipulation

Seaborn & Matplotlib: Exploratory Visualization

SciPy: Statistical Testing (ANOVA)

Streamlit: Web Deployment

Plotly: Interactive Charting
