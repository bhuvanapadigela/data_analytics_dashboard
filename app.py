import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# Load Data
# -------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

df = load_data()

# -------------------------------
# Dashboard Title
# -------------------------------
st.title("📊 Simple Data Analytics Dashboard")

# -------------------------------
# Show Raw Data
# -------------------------------
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.dataframe(df)

# -------------------------------
# Filters
# -------------------------------
st.sidebar.header("Filters")
numeric_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

selected_col = st.sidebar.selectbox("Choose a column to visualize:", df.columns)

# -------------------------------
# Visualization
# -------------------------------
st.subheader(f"Visualization for {selected_col}")

if selected_col in numeric_cols:
    fig = px.histogram(df, x=selected_col, nbins=20, title=f"Distribution of {selected_col}")
    st.plotly_chart(fig)

elif selected_col in categorical_cols:
    fig = px.bar(df[selected_col].value_counts().reset_index(),
                 x="index", y=selected_col,
                 title=f"Count of {selected_col}")
    st.plotly_chart(fig)

# -------------------------------
# Summary Stats
# -------------------------------
st.subheader("Summary Statistics")
st.write(df.describe(include='all'))