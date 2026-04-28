African Climate Trend Analysis (2015–2026)Path to COP32 | Prepared for Ethiopia's Ministry of Environment📋 Project OverviewThis repository conducts an Exploratory Data Analysis (EDA) and Statistical Analysis of climate patterns across five key African nations: Ethiopia, Kenya, Sudan, Tanzania, and Nigeria. The goal is to provide data-driven evidence for climate adaptation strategies and policy recommendations ahead of COP32.🚀 Live DashboardThe analysis has been deployed as an interactive dashboard.View the Live App here: https://climate-challenge-week0-1.streamlit.app/🔍 Key Findings (Week 0)Heat Stress: Sudan exhibits the highest frequency of extreme heat days ($> 35$°C), requiring urgent cooling infrastructure.Statistical Significance: Conducted One-Way ANOVA across regional precipitation levels, resulting in a p-value < 0.001, confirming that observed climate variations are statistically significant and not due to random noise.Agricultural Risk: Identified high precipitation volatility in the Ethiopian Highlands, suggesting a need for increased irrigation investment.📂 Folder StructurePlaintext├── .github/workflows/   # Automated testing (if applicable)
├── app/
│   └── main.py          # Streamlit Dashboard code
├── data/
│   └── all_countries_master.csv  # Final cleaned & merged dataset
├── notebooks/
│   └── compare_countries.ipynb   # Task 3: Statistical Analysis & ANOVA
├── scripts/
│   └── data_cleaning.py          # Data pipeline and preprocessing
├── requirements.txt     # Production-ready dependencies
└── README.md            # Project documentation
🛠️ Setup & InstallationClone the repository:Bashgit clone https://github.com/arsema16/climate-challenge-week0.git
cd climate-challenge-week0
Set up Environment:Bashpython -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
Install Dependencies:Bashpip install -r requirements.txt
🧪 Technologies UsedPython 3.10+Pandas/NumPy: Data ManipulationSeaborn/Matplotlib: Exploratory VisualizationSciPy: Statistical Testing (ANOVA)Streamlit: Web DeploymentHow to update this on GitHub:Go to your repo on GitHub.Click the pencil icon (edit) on the README.md file.Delete everything and paste the text above.Scroll down and click "Commit changes".
