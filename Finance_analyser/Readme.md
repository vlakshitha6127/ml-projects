# 💰 Personal Finance Analyzer

An end-to-end data analysis project that explores a personal finance transactions dataset using Python. The project focuses on data cleaning, exploratory data analysis (EDA), and generating meaningful financial insights through visualizations.

---

## 📌 Project Overview

Raw financial datasets often contain missing values, duplicate records, inconsistent formatting, and spelling errors. This project demonstrates a complete data analysis workflow by transforming messy transaction data into a clean, analysis-ready dataset and uncovering spending patterns through visualizations.

---

## 🎯 Objectives

- Assess data quality
- Clean and preprocess the dataset
- Handle missing values and duplicates
- Standardize inconsistent categorical values
- Perform exploratory data analysis
- Generate meaningful financial insights

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- RapidFuzz
- Jupyter Notebook

---

## 📂 Dataset

The dataset contains personal financial transactions with information such as:

- Transaction ID
- User ID
- Date
- Transaction Type
- Category
- Amount
- Payment Mode
- Location
- Notes

---

## 🧹 Data Cleaning

The following preprocessing steps were performed:

- Removed duplicate records
- Handled missing values
- Converted data types
- Cleaned currency symbols and comma separators
- Standardized text formatting
- Corrected spelling inconsistencies using RapidFuzz
- Applied manual mapping for ambiguous values
- Verified the cleaned dataset

---

## 📊 Exploratory Data Analysis

The project includes visualizations and analysis for:

- Financial Overview
- Income vs Expense Analysis
- Expense Category Analysis
- Monthly Income & Expense Trends
- Payment Mode Analysis
- Location-wise Analysis
- Transaction Amount Distribution
- Outlier Detection

---

## 💡 Key Insights

- Compared overall income and expenses.
- Identified major spending categories.
- Analyzed monthly financial trends.
- Studied payment method preferences.
- Examined geographical transaction patterns.
- Investigated the distribution of transaction amounts.

---

## 📁 Project Structure

```
Personal-Finance-Analyzer/
│
├── data/
│   └── expenses.csv
│
├── notebooks/
│   └── Finance_Analyzer.ipynb
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 How to Run

1. Clone the repository

```bash
git clone https://github.com/<your-username>/personal-finance-analyzer.git
```

2. Install the required libraries

```bash
pip install -r requirements.txt
```

3. Launch Jupyter Notebook

```bash
jupyter notebook
```

4. Open the notebook and run all cells.

---

## 📷 Sample Visualizations

The notebook includes visualizations such as:

- Financial Overview
- Expense Category Distribution
- Monthly Income & Expense Trends
- Payment Mode Distribution
- Location-wise Spending
- Transaction Amount Distribution

---

## 📈 Future Improvements

- Build an interactive dashboard using Streamlit or Power BI
- Add budget prediction models
- Integrate real banking transaction data
- Develop anomaly detection for unusual expenses

---

## 👩‍💻 Author

**Lakshitha V**

Computer Science Engineering Student

Passionate about Data Analytics, Machine Learning, and AI.

---