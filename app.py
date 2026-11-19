import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Real Estate Buyer Intelligence",
    layout="wide"
)

st.title("Real Estate Buyer Segmentation Dashboard")
st.subheader("Machine Learning Based Market Intelligence")

# Load dataset
base_path = Path(__file__).parent

possible_files = [
    base_path / "data" / "Final_Real_Estate_Buyer_Segmentation.csv",
    base_path / "Final_Real_Estate_Buyer_Segmentation.csv"
]

DATA_FILE = next((f for f in possible_files if f.exists()), None)

if DATA_FILE is None:
    st.error("Dataset not found. Please check the CSV file location.")
    st.stop()

df = pd.read_csv(DATA_FILE)

# Sidebar filters
st.sidebar.header("Dashboard Filters")

# Country
countries = sorted(df["country"].dropna().unique())
selected_countries = st.sidebar.multiselect(
    "Select Country", countries, default=countries
)

# Region
regions = sorted(df["region"].dropna().unique())
selected_regions = st.sidebar.multiselect(
    "Select Region", regions, default=regions
)

# Acquisition Purpose
purposes = sorted(df["acquisition_purpose"].dropna().unique())
selected_purposes = st.sidebar.multiselect(
    "Select Acquisition Purpose", purposes, default=purposes
)

# Client Type
client_types = sorted(df["client_type"].dropna().unique())
selected_client_types = st.sidebar.multiselect(
    "Select Client Type", client_types, default=client_types
)

# Apply first four filters
filtered_df = df[
    df["country"].isin(selected_countries)
    & df["region"].isin(selected_regions)
    & df["acquisition_purpose"].isin(selected_purposes)
    & df["client_type"].isin(selected_client_types)
].copy()

# Buyer Segment
st.sidebar.subheader("Buyer Segment")

segments = sorted(filtered_df["Buyer_Segment"].dropna().unique())

selected_segments = st.sidebar.multiselect(
    "Select Buyer Segment",
    segments,
    default=segments
)

filtered_df = filtered_df[
    filtered_df["Buyer_Segment"].isin(selected_segments)
]

# KPIs
total_buyers = len(filtered_df)

investment_buyers = (
    filtered_df["acquisition_purpose"] == "Investment"
).sum()

loan_applicants = (
    filtered_df["loan_applied"] == "Yes"
).sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Buyers", total_buyers)
col2.metric("Investment Buyers", int(investment_buyers))
col3.metric("Loan Applicants", int(loan_applicants))

st.divider()

# Buyer Segment Distribution
st.subheader("Buyer Segment Distribution")

fig = px.histogram(
    filtered_df,
    x="Buyer_Segment",
    title="Number of Buyers in Each Segment"
)
st.plotly_chart(fig, use_container_width=True)

# Age Distribution
st.subheader("Buyer Age Distribution")

fig = px.histogram(
    filtered_df,
    x="age",
    nbins=20,
    title="Age Distribution of Buyers"
)
st.plotly_chart(fig, use_container_width=True)

# Geographic Analysis
st.subheader("Geographic Buyer Analysis")

country_data = (
    filtered_df["country"]
    .value_counts()
    .reset_index()
)

country_data.columns = ["Country", "Buyers"]

fig = px.bar(
    country_data,
    x="Country",
    y="Buyers",
    title="Buyers by Country"
)
st.plotly_chart(fig, use_container_width=True)

# Dataset Preview
st.subheader("Buyer Dataset Preview")
st.dataframe(filtered_df.head(10), use_container_width=True)
