import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("final_stock_dataset.csv")
df['Date'] = pd.to_datetime(df['Date'])

st.set_page_config(page_title="📈 TCS Stock Dashboard", layout="wide")

st.title("📊 TCS Stock Market Dashboard")

# KPIs
latest = df.iloc[-1]

col1, col2, col3 = st.columns(3)
col1.metric("📌 Latest Close", f"₹{latest['Tata Close']:.2f}")
col2.metric("📉 Daily Return %", f"{latest['Daily Return %']:.2f}%")
col3.metric("📈 10-Day Volatility", f"{latest['Volatility_10']:.2f}")

st.markdown("---")

# Line Chart - Price Trends
st.subheader("📈 Price Trend")
price_option = st.selectbox("Select Price Type", ['Tata Open', 'Tata High', 'Tata Low', 'Tata Close', 'Tata Adj Close'])

fig, ax = plt.subplots(figsize=(10, 4))
sns.lineplot(data=df, x='Date', y=price_option, ax=ax)
ax.set_title(f"{price_option} Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Moving Averages
st.subheader("📉 Moving Averages")
fig2, ax2 = plt.subplots(figsize=(10, 4))
sns.lineplot(data=df, x='Date', y='Tata Close', label='Tata Close', ax=ax2)
sns.lineplot(data=df, x='Date', y='MA_10', label='MA 10', ax=ax2)
sns.lineplot(data=df, x='Date', y='MA_30', label='MA 30', ax=ax2)
ax2.set_title("Moving Averages")
ax2.set_xlabel("Date")
ax2.set_ylabel("Price")
ax2.legend()
ax2.tick_params(axis='x', rotation=45)
st.pyplot(fig2)

# Volume
st.subheader("🔁 Volume Traded")
fig3, ax3 = plt.subplots(figsize=(10, 4))
sns.lineplot(data=df, x='Date', y='Tata Volume', ax=ax3, color='purple')
ax3.set_title("Volume Over Time")
ax3.set_xlabel("Date")
ax3.set_ylabel("Volume")
ax3.tick_params(axis='x', rotation=45)
st.pyplot(fig3)

# Data Table
st.subheader("📄 Preview Dataset")
st.dataframe(df.tail(20))
