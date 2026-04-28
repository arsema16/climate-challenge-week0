import pandas as pd
import numpy as np
import os
from scipy import stats

# List of the countries for Task 3
countries = ['kenya', 'sudan', 'tanzania', 'nigeria']

def clean_country_data(name):
    print(f"--- Cleaning data for {name.upper()} ---")
    
    # 1. Load the raw data
    try:
        df = pd.read_csv(f'data/{name}.csv')
    except FileNotFoundError:
        print(f"File for {name} not found in data/ folder. Skipping.")
        return

    # 2. Basic Setup
    df['Country'] = name.capitalize()
    df['Date'] = pd.to_datetime(df['YEAR'] * 1000 + df['DOY'], format='%Y%j')
    df['Month'] = df['Date'].dt.month

    # 3. Handling the -999 'NASA Sludge'
    df.replace(-999, np.nan, inplace=True)
    
    # 4. Removing Duplicates
    initial_rows = len(df)
    df.drop_duplicates(inplace=True)
    print(f"Removed {initial_rows - len(df)} duplicate rows.")

    # 5. Outlier Check (KPI requirement)
    cols = ['T2M', 'PRECTOTCORR', 'RH2M']
    z_scores = np.abs(stats.zscore(df[cols].dropna()))
    print(f"Outliers detected in {name}: {(z_scores > 3).sum()}")

    # 6. Fill missing values 
    df.ffill(inplace=True)

    # 7. Export the cleaned version
    output_file = f'data/{name}_clean.csv'
    df.to_csv(output_file, index=False)
    print(f"Successfully saved to {output_file}\n")

# loop for the remaining 4 countries
for c in countries:
    clean_country_data(c)