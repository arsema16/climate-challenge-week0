import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="COP32 Climate Analytics", layout="wide")

st.title("🌍 African Climate Trend Analysis (COP32)")

# Path logic for Streamlit
data_path = os.path.join('data', 'all_countries_master.csv')

@st.cache_data
def load_data():
    return pd.read_csv(data_path)

try:
    df = load_data()
    df['date'] = pd.to_datetime(df['date'])

    # Sidebar
    st.sidebar.header("Dashboard Filters")
    countries = st.sidebar.multiselect("Select Countries", options=df['country'].unique(), default=df['country'].unique())
    year_range = st.sidebar.slider("Select Year Range", 2015, 2026, (2015, 2026))

    # Filtering
    mask = (df['country'].isin(countries)) & (df['date'].dt.year >= year_range[0]) & (df['date'].dt.year <= year_range[1])
    filtered_df = df[mask]

    # Metrics
    c1, c2 = st.columns(2)
    c1.metric("Average Temperature", f"{filtered_df['t2m'].mean():.2f} °C")
    c2.metric("Rainfall Volatility (Std Dev)", f"{filtered_df['prectotcorr'].std():.2f}")

    # Plot
    st.subheader("Temperature Trends Over Time")
    fig = px.line(filtered_df, x='date', y='t2m', color='country', labels={'t2m': 'Temp (°C)', 'date': 'Year'})
    st.plotly_chart(fig, use_container_width=True)

except FileNotFoundError:
    st.error("Master data file not found. Please run the Task 3 notebook first!")