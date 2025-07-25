# 📊 SmartSpend Copilot – AI-Powered Personal Finance Analyzer

**SmartSpend Copilot** is a data analysis tool that helps users gain actionable financial insights from their personal spending data. Built using **Python, Streamlit**, and **Google Gemini Pro**, it combines traditional data exploration with conversational GenAI assistance.

---

## 🚀 Features

### 🧠 AI Copilot (Gemini Pro)
- Ask natural language questions about your expenses, income, savings, or trends
- Get instantly generated insights like:
  - “Where am I overspending?”
  - “What are my top 3 expense categories this month?”
  - “How much did I save last quarter?”

### 📊 Streamlit App Highlights
- Upload your **personal finance CSV**
- Auto-generated insights:
  - Total Income, Expense, and Net Savings
  - Top Expense Categories
  - Monthly Expense Trend
- Built-in correlation and summary stats
- Gemini-powered Q&A interface

### 📈 Jupyter Notebook (SmartspendEDA.ipynb)
- Step-by-step Exploratory Data Analysis (EDA)
- Visualizations using Seaborn and Matplotlib:
  - Distribution of transaction amounts
  - Top 10 expense categories
  - Monthly trend charts
  - Income vs Expense pie chart
  - Boxplot by transaction type

---

## 🛠 Tech Stack

- `Python`
- `Streamlit`
- `Pandas`, `Seaborn`, `Matplotlib`
- `Google Generative AI (Gemini Pro)`
- `Jupyter Notebook`

---

## 📁 Project Structure

Smartspend-Copilot/
├── smartspend_app.py              # Streamlit app with Gemini Copilot
├── SmartspendEDA.ipynb            # EDA notebook with visualizations
├── README.md                      # Project documentation
└── .streamlit/
    └── secrets.toml               # Gemini API key (not pushed to GitHub)

## ▶️ Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/atharva-0932/Smartspend-copilot.git
   cd Smartspend-copilot
   pip install -r requirements.txt
   GEMINI_API_KEY = "your_api_key_here"
   streamlit run smartspend_app.py
## 📌 Future Enhancements

- Extend to support general EDA on any dataset
- Export insights as PDF/Excel reports
- Add login for saving user history
- Deploy with autosave & theme options
## 👤 Author

**Atharva Sawant**  
[🔗 Email:atharvasawant246@gmail.com]
