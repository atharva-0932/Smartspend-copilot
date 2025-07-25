# Streamlit-based SmartSpend Copilot Starter App

import streamlit as st
import pandas as pd
import google.generativeai as genai
import os

# --- Set Page Title ---
st.set_page_config(page_title="SmartSpend Copilot", layout="wide")
st.title("📊 SmartSpend: Personal Finance Copilot")

# --- Google Gemini Pro Setup ---
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"] if "GEMINI_API_KEY" in st.secrets else os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("API key for Gemini Pro not found. Please set it in your environment or .streamlit/secrets.toml")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

uploaded_file = st.file_uploader("Upload your dataset (CSV format)", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")
    st.subheader("📊 Preview of Data")
    st.dataframe(df.head())


    # --- Date Conversion ---
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df['Month'] = df['Date'].dt.strftime('%B')

    # --- Clean Columns ---
    if 'Category' in df.columns:
        df['Category'] = df['Category'].str.strip().str.title()
    if 'Type' in df.columns:
        df['Type'] = df['Type'].str.strip().str.title()
if uploaded_file is not None:
    st.subheader("🧹 Data Cleaning & Structure")
    st.write(df.info())
    st.write("Null values per column:")
    st.write(df.isnull().sum())

    st.subheader("📈 Summary Statistics")
    st.write(df.describe(include='all'))

    st.subheader("🔁 Correlation Heatmap (numeric columns)")
    numeric_df = df.select_dtypes(include='number')
    if not numeric_df.empty:
        st.write(numeric_df.corr())
import io

# Convert summary to string
summary_str = io.StringIO()
df.info(buf=summary_str)
eda_summary = summary_str.getvalue()

eda_summary += "\n\nColumn summaries:\n"
eda_summary += str(df.describe(include='all'))

    # --- EDA Summary ---
    st.subheader("📈 Summary Statistics")
    st.dataframe(df.describe(include='all'))

    total_income = df[df['Type'] == 'Income']['Amount'].sum()
    total_expense = df[df['Type'] == 'Expense']['Amount'].sum()

    summary = f"""
    Here is the financial summary:
    - Total Income: ₹{total_income:,.2f}
    - Total Expense: ₹{total_expense:,.2f}
    - Net Savings: ₹{(total_income - total_expense):,.2f}
    - Top 3 Expense Categories: {df[df['Type'] == 'Expense']['Category'].value_counts().head(3).to_dict()}
    - Expense Trend across Months: {df.groupby('Month')['Amount'].sum().to_dict()}
    """

    st.markdown("---")
    st.subheader("💬 Ask SmartSpend Copilot")

    user_input = st.text_area("Enter your question about your finances")

    if st.button("Ask Gemini") and user_input:
        full_prompt = f"""
        Based on the following summary of financial data:

        {summary}

        Answer the following question in simple terms:
        {user_input}
        """
        with st.spinner("Thinking..."):
            response = model.generate_content(full_prompt)
            st.success("✅ Response ready!")
            st.write(response.text)

else:
    st.info("👈 Upload a CSV file to begin your analysis.")
