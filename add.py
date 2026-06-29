import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Performance System")

st.title("📊 Student Performance Web App")

df = None

# Upload CSV
uploaded_file = st.file_uploader("Upload Student CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Data Preview")
    st.write(df.head())

    # Top 10 students
    if "Performance Score" in df.columns:
        st.subheader("🏆 Top 10 Students")
        top10 = df.sort_values(by="Performance Score", ascending=False).head(10)
        st.write(top10)

    else:
        st.warning("⚠️ 'Performance Score' column not found")

    # Show full data
    if st.checkbox("Show Full Dataset"):
        st.write(df)

    # Basic stats
    if df is not None:
        st.subheader("📊 Dataset Info")
        st.write(df.describe())
