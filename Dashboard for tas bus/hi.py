import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt

st.set_page_config(layout="wide")

# Sample data
data = {
    "Order Date": [
        "2017-08-11T00:00:00",
        "2017-08-11T00:00:00",
        "2017-05-12T00:00:00",
        "2017-01-16T00:00:00",
        "2017-01-16T00:00:00",
        "2017-06-20T00:00:00",
        "2017-06-20T00:00:00",
        "2017-06-17T00:00:00",
        "2017-06-17T00:00:00",
        "2017-06-17T00:00:00",
        "2017-06-17T00:00:00",
    ],
    "Customer ID": [
        "CG-12520",
        "CG-12520",
        "IM-15070",
        "EH-13945",
        "EH-13945",
        "LH-16900",
        "LH-16900",
        "TB-21055",
        "TB-21055",
        "TB-21055",
        "TB-21055",
    ],
    "Customer Name": [
        "Claire Gute",
        "Claire Gute",
        "Irene Maddox",
        "Eric Hoffmann",
        "Eric Hoffmann",
        "Lena Hernandez",
        "Lena Hernandez",
        "Ted Butterfield",
        "Ted Butterfield",
        "Ted Butterfield",
        "Ted Butterfield",
    ],
    "Sub-Category": [
        "Chairs",
        "Machines",
        "Phones",
        "Storage",
        "Binders",
        "Chairs",
        "Machines",
        "Phones",
        "Storage",
        "Binders",
        "Chairs",
    ],
    "Region": [
        "East",
        "West",
        "Central",
        "East",
        "West",
        "Central",
        "East",
        "West",
        "Central",
        "East",
        "West",
    ],
    "Sales": [
        39000,
        34000,
        33000,
        26000,
        26000,
        39000,
        34000,
        33000,
        26000,
        26000,
        39000,
    ],
    "State": [
        "California",
        "New York",
        "Texas",
        "Pennsylvania",
        "Virginia",
        "Michigan",
        "Ohio",
        "Washington",
        "Illinois",
        "California",
        "New York",
    ],
    "City": [
        "Los Angeles",
        "New York",
        "Houston",
        "Philadelphia",
        "Richmond",
        "Detroit",
        "Columbus",
        "Seattle",
        "Chicago",
        "San Francisco",
        "Brooklyn",
    ],
}

df = pd.DataFrame(data)
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create the Streamlit dashboard

# Title
st.title("Sales Scorecard")

# Side bar for filtering
st.sidebar.header("Filter Options")

# Filter by Year
year_filter = st.sidebar.slider("Year", min_value=2010, max_value=2017, value=2017, step=1)
df_filtered = df[df["Order Date"].dt.year == year_filter]

# Filter by Segment
segment_filter = st.sidebar.multiselect("Segment", options=["Consumer", "Corporate", "Home Office"])
if segment_filter:
    df_filtered = df_filtered[df_filtered["Region"].isin(segment_filter)]

# Main Dashboard
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Sales by Sub-Category")
    st.write(
        alt.Chart(df_filtered)
        .mark_bar()
        .encode(
            alt.X("Sub-Category:N", sort="-y"),
            alt.Y("sum(Sales):Q", title="Total Sales"),
            alt.Color("Region:N", scale=alt.Scale(scheme="tableau10")),
        )
        .properties(height=300, width=400)
    )

with col2:
    st.header("Sales by Category")
    df_category = (
        df_filtered.groupby("Sub-Category")["Sales"]
        .sum()
        .reset_index(name="Total Sales")
    )

    fig = px.pie(df_category, values="Total Sales", names="Sub-Category")
    st.plotly_chart(fig, use_container_width=True)

with col3:
    st.header("Sales Trend")
    df_trend = df_filtered.groupby(df_filtered["Order Date"].dt.strftime("%B"))["Sales"].sum().reset_index()

    st.write(
        alt.Chart(df_trend)
        .mark_line()
        .encode(
            alt.X("Order Date:T", title="Month"),
            alt.Y("sum(Sales):Q", title="Total Sales"),
        )
        .properties(height=300, width=400)
    )

# Dashboard KPIs
st.header("Key Performance Indicators (KPIs)")

# Create KPIs
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Current Year Sales", "$" + str(df_filtered["Sales"].sum()), "30.64%")

with col2:
    st.metric("Previous Year Sales", "$" + str(df_filtered["Sales"].sum()), "30.64%")

with col3:
    st.metric("Year-on-Year Growth", "30.64%", "30.64%")

# Sales by State and City
st.header("Sales by State and City")

df_state = (
    df_filtered.groupby(["State", "City"])["Sales"]
    .sum()
    .reset_index(name="Total Sales")
)

st.write(
    alt.Chart(df_state)
    .mark_circle()
    .encode(
        alt.X("State:N", title="State"),
        alt.Y("City:N", title="City"),
        alt.Size("Total Sales:Q", scale=alt.Scale(range=[10, 100])),
        alt.Color("Total Sales:Q", scale=alt.Scale(scheme="redblue")),
        alt.Tooltip(["State", "City", "Total Sales"]),
    )
    .properties(height=300, width=400)
)

st.markdown("---")

st.markdown("**Data Source:**  Sample data.")
st.markdown("**Note:** This is a basic example and can be further customized to meet specific requirements.")
