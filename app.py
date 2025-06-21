import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="📈 TCS Stock Dashboard", layout="centered")
st.title("📈 TCS Stock Forecast Dashboard")

try:
    # Load the dataset
    df = pd.read_csv("final_stock_dataset.csv")

    # Clean column names (remove BOM characters, trim spaces)
    df.columns = df.columns.str.strip().str.replace('\ufeff', '')

    # Show column names for debugging
    st.subheader("📋 Columns in Dataset")
    st.write(df.columns.tolist())

    # Handle Date column
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    else:
        # Generate synthetic dates if missing
        df['Date'] = pd.date_range(start="2020-01-01", periods=len(df), freq='D')

    # Check for 'Tata Close' column
    if 'Tata Close' not in df.columns:
        st.error("❌ 'Tata Close' column not found in the dataset.")
        st.stop()

    # Display DataFrame
    st.subheader("📄 Data Preview")
    st.dataframe(df.head())

    # Plotting Tata Close over Date
    st.subheader("📊 Tata Close Price Over Time")
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Tata Close'], color='green', linewidth=2)
    ax.set_title("Tata Close Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Tata Close Price")
    st.pyplot(fig)

except FileNotFoundError:
    st.error("❌ File 'final_stock_dataset.csv' not found. Please ensure it's in the project folder.")
except Exception as e:
    st.error(f"❌ An unexpected error occurred: {e}")
