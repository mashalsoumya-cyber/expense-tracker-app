"""
Visualization Module
====================
This module creates professional charts and visualizations for expense data.

Functions:
- category_bar_chart(): Creates category-wise spending bar chart
- expense_pie_chart(): Creates expense distribution pie chart
- monthly_trend_chart(): Creates monthly income vs expense trend
- weekday_count_chart(): Creates transaction count by weekday
- save_all_visualizations(): Runs all visualization functions

Output:
- PNG files saved in outputs/ directory

Author: Your Name
Date: 2026-04-16
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style for professional-looking charts
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

def ensure_output_dir(output_dir='outputs'):
    """Create output directory if it doesn't exist."""
    os.makedirs(output_dir, exist_ok=True)


def category_bar_chart(df, output_path='outputs/01_category_total.png'):
    """
    Create bar chart showing total spending by category.
    
    Args:
        df (pd.DataFrame): Cleaned expense DataFrame
        output_path (str): Path to save the chart
    """
    print("📊 Creating Category Bar Chart...")
    ensure_output_dir()
    
    expense_df = df[df['Type'] == 'Expense']
    category_sum = expense_df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(12, 6))
    bars = plt.bar(category_sum.index, category_sum.values, color=sns.color_palette('Set2', len(category_sum)))
    plt.title('💰 Total Expense by Category', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Category', fontsize=12, fontweight='bold')
    plt.ylabel('Total Spent (₹)', fontsize=12, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'₹{int(height):,}', ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Saved: {output_path}")
    plt.close()


def expense_pie_chart(df, output_path='outputs/02_category_pie.png'):
    """
    Create pie chart showing expense distribution by category.
    
    Args:
        df (pd.DataFrame): Cleaned expense DataFrame
        output_path (str): Path to save the chart
    """
    print("🍰 Creating Expense Distribution Pie Chart...")
    ensure_output_dir()
    
    expense_df = df[df['Type'] == 'Expense']
    category_expense = expense_df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 8))
    colors = sns.color_palette('Set3', len(category_expense))
    wedges, texts, autotexts = plt.pie(
        category_expense, 
        labels=category_expense.index, 
        autopct='%1.1f%%', 
        startangle=140,
        colors=colors,
        textprops={'fontsize': 10}
    )
    
    # Enhance percentage text
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)
    
    plt.title('🥧 Expense Distribution by Category', fontsize=16, fontweight='bold', pad=20)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Saved: {output_path}")
    plt.close()


def monthly_trend_chart(df, output_path='outputs/03_monthly_trend.png'):
    """
    Create line chart showing monthly income vs expense trends.
    
    Args:
        df (pd.DataFrame): Cleaned expense DataFrame
        output_path (str): Path to save the chart
    """
    print("📈 Creating Monthly Trend Chart...")
    ensure_output_dir()
    
    monthly_expense = df[df['Type'] == 'Expense'].groupby('Month_Num')['Amount'].sum()
    monthly_income = df[df['Type'] == 'Income'].groupby('Month_Num')['Amount'].sum()
    
    plt.figure(figsize=(14, 7))
    plt.plot(monthly_expense.index, monthly_expense.values, marker='o', 
            linewidth=2.5, markersize=8, label='💸 Expense', color='#e74c3c')
    plt.plot(monthly_income.index, monthly_income.values, marker='s', 
            linewidth=2.5, markersize=8, label='💰 Income', color='#27ae60')
    
    plt.title('📊 Monthly Income vs Expense Trend', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Month (1-12)', fontsize=12, fontweight='bold')
    plt.ylabel('Amount (₹)', fontsize=12, fontweight='bold')
    plt.legend(fontsize=11, loc='best')
    plt.grid(True, alpha=0.3)
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    
    # Format y-axis as currency
    ax = plt.gca()
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{int(x/1000)}K'))
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Saved: {output_path}")
    plt.close()


def weekday_count_chart(df, output_path='outputs/04_weekday_count.png'):
    """
    Create bar chart showing transaction count by weekday.
    
    Args:
        df (pd.DataFrame): Cleaned expense DataFrame
        output_path (str): Path to save the chart
    """
    print("📆 Creating Weekday Count Chart...")
    ensure_output_dir()
    
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekday_counts = df['Weekday'].value_counts().reindex(weekday_order)
    
    plt.figure(figsize=(12, 6))
    bars = plt.bar(range(len(weekday_counts)), weekday_counts.values, 
                   color=sns.color_palette('coolwarm', len(weekday_counts)))
    plt.title('📅 Transactions by Weekday', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Weekday', fontsize=12, fontweight='bold')
    plt.ylabel('Number of Transactions', fontsize=12, fontweight='bold')
    plt.xticks(range(len(weekday_counts)), weekday_order, rotation=45, ha='right')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Saved: {output_path}")
    plt.close()


def income_expense_comparison(df, output_path='outputs/05_income_expense_comparison.png'):
    """
    Create side-by-side comparison of income and expense.
    
    Args:
        df (pd.DataFrame): Cleaned expense DataFrame
        output_path (str): Path to save the chart
    """
    print("💵 Creating Income vs Expense Comparison...")
    ensure_output_dir()
    
    total_income = df[df['Type'] == 'Income']['Amount'].sum()
    total_expense = df[df['Type'] == 'Expense']['Amount'].sum()
    
    plt.figure(figsize=(10, 6))
    categories = ['Income', 'Expense']
    values = [total_income, total_expense]
    colors = ['#27ae60', '#e74c3c']
    
    bars = plt.bar(categories, values, color=colors, width=0.6)
    plt.title('💰 Total Income vs Expense Comparison', fontsize=16, fontweight='bold', pad=20)
    plt.ylabel('Amount (₹)', fontsize=12, fontweight='bold')
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'₹{int(height/100000):.1f}L', ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    # Format y-axis
    ax = plt.gca()
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₹{int(x/100000)}L'))
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Saved: {output_path}")
    plt.close()


def payment_method_chart(df, output_path='outputs/06_payment_method.png'):
    """
    Create bar chart showing payment method usage.
    
    Args:
        df (pd.DataFrame): Cleaned expense DataFrame
        output_path (str): Path to save the chart
    """
    print("💳 Creating Payment Method Chart...")
    ensure_output_dir()
    
    payment_counts = df['Payment Method'].value_counts().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(payment_counts.index, payment_counts.values, 
                   color=sns.color_palette('husl', len(payment_counts)))
    plt.title('💳 Payment Method Usage', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Payment Method', fontsize=12, fontweight='bold')
    plt.ylabel('Number of Transactions', fontsize=12, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Saved: {output_path}")
    plt.close()


def save_all_visualizations(input_path='data/cleaned_expenses.csv'):
    """
    Create and save all visualizations.
    
    Args:
        input_path (str): Path to cleaned CSV file
    """
    print("\n🎨 Starting Visualization Generation...\n")
    
    # Load data
    df = pd.read_csv(input_path)
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Generate all charts
    category_bar_chart(df)
    expense_pie_chart(df)
    monthly_trend_chart(df)
    weekday_count_chart(df)
    income_expense_comparison(df)
    payment_method_chart(df)
    
    print("\n✨ All visualizations saved to 'outputs/' directory!")
    print("📁 Check outputs/ folder for PNG files")


if __name__ == "__main__":
    save_all_visualizations()