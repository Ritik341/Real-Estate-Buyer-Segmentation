# Sidebar filters
st.sidebar.header("Dashboard Filters")

# Country filter
countries = sorted(df["country"].dropna().unique())
selected_countries = st.sidebar.multiselect(
    "Select Country", countries, default=countries
)

# Region filter
regions = sorted(df["region"].dropna().unique())
selected_regions = st.sidebar.multiselect(
    "Select Region", regions, default=regions
)

# Acquisition Purpose filter
purposes = sorted(df["acquisition_purpose"].dropna().unique())
selected_purposes = st.sidebar.multiselect(
    "Select Acquisition Purpose", purposes, default=purposes
)

# Client Type filter
client_types = sorted(df["client_type"].dropna().unique())
selected_client_types = st.sidebar.multiselect(
    "Select Client Type", client_types, default=client_types
)

# Apply filters
df = df[
    df["country"].isin(selected_countries) &
    df["region"].isin(selected_regions) &
    df["acquisition_purpose"].isin(selected_purposes) &
    df["client_type"].isin(selected_client_types)
]

# Buyer Segment filter
st.sidebar.subheader("Buyer Segment")

segments = df["Buyer_Segment"].dropna().unique()

selected_segments = st.sidebar.multiselect(
    "Select Buyer Segment",
    segments,
    default=list(segments)
)

df = df[df["Buyer_Segment"].isin(selected_segments)]
