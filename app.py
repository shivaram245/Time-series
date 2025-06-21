import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 TCS Stock Forecast Dashboard")

# Step 1: Load the CSV
try:
    df = pd.read_csv("final_stock_dataset.csv")
    
    # Step 2: Show the actual columns
    st.write("Columns in your dataset:", df.columns.tolist())

    # Step 3: Clean up column names
    df.columns = df.columns.str.strip().str.replace('\ufeff', '')

    # Step 4: Rename any Date-like column
    for col in df.columns:
        if col.lower().startswith("date"):
            df.rename(columns={col: "Date"}, inplace=True)
            break

    # Step 5: Convert Date or fallback to index
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
    else:
        df["Date"] = range(len(df))  # fallback to index as pseudo-date

    # Step 6: Display data
    st.subheader("📋 Dataset Preview")
    st.dataframe(df.head())

    # Step 7: Plot
    st.subheader("📊 Tata Close Over Time")
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Tata_Close"], color='blue')
    ax.set_xlabel("Date")
    ax.set_ylabel("Tata Close")
    st.pyplot(fig)

except Exception as e:
    st.error(f"Something went wrong: {e}")
