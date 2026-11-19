
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Real Estate Buyer Intelligence",
    layout="wide"
)

st.title("Real Estate Buyer Segmentation Dashboard")
st.subheader("Machine Learning Based Market Intelligence")

from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "Final_Real_Estate_Buyer_Segmentation.csv"
if not DATA_FILE.exists():
    DATA_FILE = Path(__file__).parent / "Final_Real_Estate_Buyer_Segmentation.csv"

if not DATA_FILE.exists():
    st.error("Dataset file not found. Keep the data folder next to app.py.")
    st.stop()

df = pd.read_csv(DATA_FILE)

# Sidebar filters
st.sidebar.header("Dashboard Filters")

segments = df["Buyer_Segment"].dropna().unique()

selected_segments = st.sidebar.multiselect(
    "Select Buyer Segment",
    segments,
    default=list(segments)
)

df = df[df["Buyer_Segment"].isin(selected_segments)]

# KPI calculations
total_buyers = len(df)
investment_buyers = (df["acquisition_purpose"] == "Investment").sum()
loan_applicants = (df["loan_applied"] == "Yes").sum()

# KPI cards
st.markdown(f"""
<div style="display:flex;gap:15px;">
<div style="background:#26364a;padding:20px;border-radius:10px;flex:1;">
<h4>Total Buyers</h4><h2>{total_buyers}</h2>
</div>
<div style="background:#26364a;padding:20px;border-radius:10px;flex:1;">
<h4>Investment Buyers</h4><h2>{investment_buyers}</h2>
</div>
<div style="background:#26364a;padding:20px;border-radius:10px;flex:1;">
<h4>Loan Applicants</h4><h2>{loan_applicants}</h2>
</div>
</div>
""", unsafe_allow_html=True)

st.divider()

# Buyer segmentation
st.subheader("Buyer Segment Distribution")

fig = px.histogram(
    df,
    x="Buyer_Segment",
    color="Buyer_Segment",
    title="Number of Buyers in Each Segment"
)
st.plotly_chart(fig, use_container_width=True)

# Age distribution
st.subheader("Buyer Age Distribution")

fig = px.histogram(
    df,
    x="age",
    nbins=20,
    title="Age Distribution of Buyers"
)
st.plotly_chart(fig, use_container_width=True)

# Geographic analysis
st.subheader("Geographic Buyer Analysis")

country_data = df["country"].value_counts().reset_index()
country_data.columns = ["Country", "Buyers"]

fig = px.bar(
    country_data,
    x="Country",
    y="Buyers",
    title="Buyers by Country"
)
st.plotly_chart(fig, use_container_width=True)

# Dataset preview
st.subheader("Buyer Dataset Preview")
st.code(df.head(10).to_string(index=False))