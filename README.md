# 💰 Expense Tracker App using Data Science

> A complete, beginner-to-industry grade project for tracking, analyzing, and visualizing personal expenses using Python.

## 🎯 Project Overview

This project demonstrates a **data-driven approach to expense management** by building a system that:
- ✅ Collects and stores expense data
- ✅ Cleans and preprocesses data for accuracy
- ✅ Analyzes spending patterns and trends
- ✅ Visualizes insights through professional charts
- ✅ Generates actionable recommendations

Perfect for **internship/placement portfolios** and learning **end-to-end data science workflows**.

---

## 🚩 Problem Statement

**Individuals and businesses struggle with:**
- 📊 Understanding where money is being spent
- 🔍 Identifying spending patterns and anomalies
- 📈 Making data-driven financial decisions
- 💡 Creating actionable budgets and savings plans

**Raw transaction logs are messy and unorganized** → Hard to extract insights → Poor financial decisions.

---

## 💡 Solution

Build a **data pipeline** that:
1. Accepts expense data (manual input or CSV)
2. Cleans and standardizes the data
3. Performs exploratory data analysis (EDA)
4. Creates professional visualizations
5. Generates insights and recommendations

**Output:** A user can understand their spending habits and make informed financial decisions.

---

## 🔥 Key Features

| Feature | Description |
|---------|-------------|
| 📊 **Synthetic Data Generation** | Creates realistic expense transactions for testing |
| 🧹 **Data Cleaning** | Removes duplicates, handles missing values, standardizes formats |
| 📈 **EDA Analysis** | Category-wise, monthly, and weekday-based analysis |
| 🎨 **Professional Visualizations** | Bar charts, pie charts, line graphs, comparisons |
| 💡 **Intelligent Insights** | Overspending alerts, top categories, recommendations |
| 🚀 **Complete Pipeline** | Single script runs the entire workflow |

---

## 🧰 Tech Stack

| Component | Tools |
|-----------|-------|
| **Language** | Python 3.x |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Dashboard (Optional)** | Streamlit |
| **Development** | Jupyter Notebook / VS Code |

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/SoumyaMashal/Expense-Tracker-App.git
cd Expense-Tracker-App
```

### 2. Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Quick Start

### Run the Complete Pipeline
```bash
python main.py
```

This single command executes:
1. ✅ Data Generation
2. ✅ Data Cleaning
3. ✅ EDA Analysis
4. ✅ Visualization Creation
5. ✅ Insights Generation

**Expected Output:**
- Generated data in `data/` folder
- Visualizations in `outputs/` folder
- Insights report in `outputs/insights_report.txt`

### Run Individual Modules
```bash
# Data Generation Only
python src/data_creation.py

# Data Cleaning Only
python src/data_cleaning.py

# Analysis Only
python src/eda_analysis.py

# Visualizations Only
python src/visualizations.py

# Insights Only
python src/insights_generator.py
```

### Run Streamlit Dashboard (Optional)
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Expense-Tracker-App/
│
├── data/
│   ├── expenses.csv              # Raw synthetic data
│   └── cleaned_expenses.csv      # Processed data
│
├── src/
│   ├── data_creation.py          # Generate synthetic data
│   ├── data_cleaning.py          # Clean & preprocess
│   ├── eda_analysis.py           # Analyze patterns
│   ├── visualizations.py         # Create charts
│   └── insights_generator.py     # Generate insights
│
├── outputs/
│   ├── 01_category_total.png     # Bar chart
│   ├── 02_category_pie.png       # Pie chart
│   ├── 03_monthly_trend.png      # Line chart
│   ├── 04_weekday_count.png      # Weekday analysis
│   ├── 05_income_expense_comparison.png
│   ├── 06_payment_method.png
│   └── insights_report.txt       # Text report
│
├── images/                        # Screenshots for README
├── notebooks/                     # Jupyter notebooks (optional)
├── app.py                         # Streamlit dashboard (optional)
├── main.py                        # Complete pipeline executor
├── requirements.txt               # Dependencies
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

---

## 📊 Sample Output

### 1. Category-wise Spending
```
Food        ₹25,000  (30%)
Transport   ₹15,000  (18%)
Rent        ₹20,000  (24%)
Entertainment ₹12,000 (14%)
Bills       ₹10,000  (12%)
```

### 2. Monthly Trend
```
Month 1: Income ₹50,000 | Expense ₹35,000 ✅
Month 2: Income ₹50,000 | Expense ₹52,000 ⚠️
Month 3: Income ₹50,000 | Expense ₹41,000 ✅
```

### 3. Key Insights
- 💡 Top spending category: **Food (30%)**
- 📈 Highest spending month: **Month 2 (₹52,000)**
- ⚠️ Overspent in: **1 month**
- ✅ Savings rate: **18%**

---

## 📸 Screenshots

### Visualization Examples

**Category-wise Bar Chart:**  
![Category Total](outputs/01_category_total.png)

**Expense Distribution Pie Chart:**  
![Category Pie](outputs/02_category_pie.png)

**Monthly Income vs Expense Trend:**  
![Monthly Trend](outputs/03_monthly_trend.png)

**Transaction Count by Weekday:**  
![Weekday Count](outputs/04_weekday_count.png)

---

## 🎓 Learning Outcomes

By completing this project, you'll learn:

✅ **Data Science Concepts:**
- Data collection and generation
- Data cleaning & preprocessing
- Exploratory data analysis (EDA)
- Statistical analysis
- Data visualization

✅ **Python Skills:**
- Pandas for data manipulation
- NumPy for numerical operations
- Matplotlib & Seaborn for plotting
- File I/O and CSV handling

✅ **Industry Skills:**
- End-to-end project workflow
- GitHub version control
- Professional documentation
- Report generation

---


## 🔮 Future Enhancements

- 📱 **Mobile App** - Flutter/React Native app for on-the-go tracking
- 🔗 **Bank API Integration** - Auto-import transactions from bank accounts
- 🤖 **ML Predictions** - Predict future spending patterns using time series analysis
- 📢 **Alert System** - Send notifications for budget overages
- 🎯 **Goal Tracking** - Set and monitor savings goals
- 💾 **Database** - Replace CSV with SQLite/PostgreSQL for scalability
- ☁️ **Cloud Deployment** - Host on AWS/Heroku for public access

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'pandas'` | Run `pip install -r requirements.txt` |
| `FileNotFoundError: data/expenses.csv` | Run `python src/data_creation.py` first |
| Plots not displaying in Jupyter | Add `%matplotlib inline` at the top |
| Streamlit app won't launch | Run `pip install streamlit` and then `streamlit run app.py` |

---

## 📚 Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn Gallery](https://seaborn.pydata.org/examples.html)
- [Streamlit Docs](https://docs.streamlit.io/)
- [Data Science Workflow](https://www.coursera.org/learn/data-science)

---


