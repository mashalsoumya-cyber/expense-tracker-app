"""
Streamlit Dashboard for Expense Tracker
========================================
Interactive dashboard for visualizing and exploring expense data.

Run with: streamlit run app.py

Features:
- Multi-select filters for categories and types
- Interactive charts
- Raw data viewer
- Summary statistics
- Auto-save charts and summary reports to outputs/ and images/

Author: Your Name
Date: 2026-04-16
"""

import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="💰 Expense Tracker Dashboard",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# FOLDER SETUP
# -----------------------------
os.makedirs("outputs", exist_ok=True)
os.makedirs("images", exist_ok=True)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    """Load cleaned expense data."""
    df = pd.read_csv("data/cleaned_expenses.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.title("🔍 Filters")
st.sidebar.markdown("---")

categories = sorted(df["Category"].unique())
selected_categories = st.sidebar.multiselect(
    "📂 Select Categories",
    options=categories,
    default=categories
)

transaction_types = ["All"] + sorted(df["Type"].unique())
selected_type = st.sidebar.selectbox(
    "🧾 Transaction Type",
    options=transaction_types
)

# Apply filters
filtered_df = df[df["Category"].isin(selected_categories)].copy()
if selected_type != "All":
    filtered_df = filtered_df[filtered_df["Type"] == selected_type].copy()

# -----------------------------
# AUTO SAVE HELPER
# -----------------------------
def save_figure(fig, filename):
    """Save the same figure in outputs and images folders."""
    output_path = os.path.join("outputs", filename)
    image_path = os.path.join("images", filename)
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    fig.savefig(image_path, dpi=300, bbox_inches="tight")

def save_summary_file(total_income, total_expense, net_savings, savings_rate, filtered_data):
    """Save dashboard summary as text and csv."""
    summary_txt_path = os.path.join("outputs", "dashboard_summary.txt")
    filtered_csv_path = os.path.join("outputs", "filtered_data.csv")

    with open(summary_txt_path, "w", encoding="utf-8") as f:
        f.write("EXPENSE TRACKER DASHBOARD SUMMARY\n")
        f.write("=" * 50 + "\n")
        f.write(f"Selected Categories: {', '.join(selected_categories) if selected_categories else 'None'}\n")
        f.write(f"Selected Transaction Type: {selected_type}\n")
        f.write("-" * 50 + "\n")
        f.write(f"Total Income  : ₹{total_income:,.2f}\n")
        f.write(f"Total Expense : ₹{total_expense:,.2f}\n")
        f.write(f"Net Savings   : ₹{net_savings:,.2f}\n")
        f.write(f"Savings Rate  : {savings_rate:.2f}%\n")
        f.write("-" * 50 + "\n")
        f.write(f"Total Filtered Records: {len(filtered_data)}\n")

    filtered_data.sort_values("Date", ascending=False).to_csv(filtered_csv_path, index=False)

# -----------------------------
# MAIN DASHBOARD
# -----------------------------
st.title("💰 Expense Tracker Dashboard")
st.markdown("Interactive analysis of your financial data")
st.markdown("---")

# -----------------------------
# ROW 1: KEY METRICS
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

total_income = filtered_df[filtered_df["Type"] == "Income"]["Amount"].sum()
total_expense = filtered_df[filtered_df["Type"] == "Expense"]["Amount"].sum()
net_savings = total_income - total_expense
savings_rate = (net_savings / total_income * 100) if total_income > 0 else 0

with col1:
    st.metric(label="💵 Total Income", value=f"₹{total_income:,.0f}")

with col2:
    st.metric(label="💸 Total Expense", value=f"₹{total_expense:,.0f}")

with col3:
    st.metric(label="💰 Net Savings", value=f"₹{net_savings:,.0f}")

with col4:
    st.metric(label="📈 Savings Rate", value=f"{savings_rate:.1f}%")

# Save summary after metrics calculation
save_summary_file(total_income, total_expense, net_savings, savings_rate, filtered_df)

st.markdown("---")

# -----------------------------
# ROW 2: CHARTS
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Spending by Category")
    category_total = (
        filtered_df[filtered_df["Type"] == "Expense"]
        .groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    if not category_total.empty:
        fig, ax = plt.subplots(figsize=(8, 4))
        category_total.plot(
            kind="bar",
            ax=ax,
            color=sns.color_palette("Set2", len(category_total))
        )
        ax.set_title("Category-wise Spending", fontsize=12, fontweight="bold")
        ax.set_xlabel("Category")
        ax.set_ylabel("Amount (₹)")
        plt.xticks(rotation=45)
        plt.tight_layout()

        save_figure(fig, "spending_by_category.png")
        st.pyplot(fig)
        plt.close(fig)
    else:
        st.info("No data available for selected filters")

with col2:
    st.subheader("🥧 Expense Distribution")
    pie_data = (
        filtered_df[filtered_df["Type"] == "Expense"]
        .groupby("Category")["Amount"]
        .sum()
    )

    if not pie_data.empty:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.pie(
            pie_data,
            labels=pie_data.index,
            autopct="%1.1f%%",
            startangle=90
        )
        ax.set_title("Expense Distribution", fontsize=12, fontweight="bold")
        plt.tight_layout()

        save_figure(fig, "expense_distribution.png")
        st.pyplot(fig)
        plt.close(fig)
    else:
        st.info("No data available for selected filters")

st.markdown("---")

# -----------------------------
# ROW 3: TRENDS
# -----------------------------
st.subheader("📈 Monthly Trend Analysis")
col1, col2 = st.columns(2)

with col1:
    monthly_expense = (
        filtered_df[filtered_df["Type"] == "Expense"]
        .groupby(filtered_df["Date"].dt.month)["Amount"]
        .sum()
    )
    monthly_income = (
        filtered_df[filtered_df["Type"] == "Income"]
        .groupby(filtered_df["Date"].dt.month)["Amount"]
        .sum()
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(
        monthly_expense.index,
        monthly_expense.values,
        marker="o",
        label="Expense",
        linewidth=2
    )
    ax.plot(
        monthly_income.index,
        monthly_income.values,
        marker="s",
        label="Income",
        linewidth=2
    )
    ax.set_title("Income vs Expense Trend", fontsize=12, fontweight="bold")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount (₹)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()

    save_figure(fig, "monthly_trend.png")
    st.pyplot(fig)
    plt.close(fig)

with col2:
    weekday_counts = filtered_df["Weekday"].value_counts()
    weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday_counts = weekday_counts.reindex(weekday_order, fill_value=0)

    fig, ax = plt.subplots(figsize=(10, 5))
    weekday_counts.plot(
        kind="bar",
        ax=ax,
        color=sns.color_palette("coolwarm", len(weekday_counts))
    )
    ax.set_title("Transactions by Weekday", fontsize=12, fontweight="bold")
    ax.set_xlabel("Weekday")
    ax.set_ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()

    save_figure(fig, "transactions_by_weekday.png")
    st.pyplot(fig)
    plt.close(fig)

st.markdown("---")

# -----------------------------
# ROW 4: DATA TABLE
# -----------------------------
st.subheader("📋 Filtered Transaction Data")

if st.checkbox("🔍 Show Raw Data"):
    st.dataframe(
        filtered_df.sort_values("Date", ascending=False),
        use_container_width=True,
        height=400
    )

# -----------------------------
# DOWNLOAD / SAVE INFO
# -----------------------------
st.markdown("---")
st.success("Charts and summary files are being saved automatically in 'outputs/' and 'images/'.")

st.markdown("""
**Saved files include:**
- outputs/spending_by_category.png
- outputs/expense_distribution.png
- outputs/monthly_trend.png
- outputs/transactions_by_weekday.png
- outputs/dashboard_summary.txt
- outputs/filtered_data.csv
- same chart images inside images/
""")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
---
**💡 Expense Tracker Dashboard v1.0**  
Built with ❤️ using Streamlit | Data Science Project
""")