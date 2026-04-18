"""
Exploratory Data Analysis (EDA) Module
========================================
This module performs comprehensive analysis of expense data.

Functions:
- category_analysis(): Analyzes spending by category
- monthly_analysis(): Analyzes trends by month
- payment_method_analysis(): Analyzes payment methods
- generate_statistics(): Creates summary statistics

Output:
- Console reports and analysis summaries

Author: Your Name
Date: 2026-04-16
"""

import pandas as pd
import numpy as np

def category_analysis(df):
    """
    Analyze spending by category.
    
    Returns:
        dict: Dictionary with category analysis results
    """
    print("\n" + "="*60)
    print("📊 CATEGORY-WISE EXPENSE ANALYSIS")
    print("="*60)
    
    expense_df = df[df['Type'] == 'Expense']
    category_stats = expense_df.groupby('Category')['Amount'].agg([
        ('Total', 'sum'),
        ('Count', 'count'),
        ('Average', 'mean'),
        ('Max', 'max'),
        ('Min', 'min')
    ]).sort_values('Total', ascending=False)
    
    print("\n📋 Spending by Category:")
    print(category_stats)
    
    # Top spending category
    top_category = category_stats['Total'].idxmax()
    top_amount = category_stats['Total'].max()
    print(f"\n🏆 Top Spending Category: {top_category} | ₹{top_amount:,.0f}")
    
    # Category percentage breakdown
    print("\n📈 Category Percentage Breakdown:")
    category_pct = (category_stats['Total'] / category_stats['Total'].sum() * 100).sort_values(ascending=False)
    for cat, pct in category_pct.items():
        print(f"   {cat:15} : {pct:6.2f}%")
    
    return category_stats


def monthly_analysis(df):
    """
    Analyze spending trends by month.
    
    Returns:
        dict: Dictionary with monthly analysis results
    """
    print("\n" + "="*60)
    print("📅 MONTHLY EXPENSE ANALYSIS")
    print("="*60)
    
    monthly_stats = df.groupby('Month_Num').agg({
        'Amount': ['sum', 'count', 'mean']
    }).round(2)
    monthly_stats.columns = ['Total', 'Count', 'Average']
    
    # Separate income and expense
    monthly_expense = df[df['Type'] == 'Expense'].groupby('Month_Num')['Amount'].sum()
    monthly_income = df[df['Type'] == 'Income'].groupby('Month_Num')['Amount'].sum()
    
    print("\n💰 Monthly Expense vs Income:")
    comparison = pd.DataFrame({
        'Expense': monthly_expense,
        'Income': monthly_income,
        'Difference': monthly_income - monthly_expense
    })
    print(comparison)
    
    # Identify overspending months
    overspent_months = comparison[comparison['Difference'] < 0]
    if not overspent_months.empty:
        print("\n🔴 OVERSPENT MONTHS (Expense > Income):")
        print(overspent_months)
    else:
        print("\n✅ No overspent months detected!")
    
    # Highest spending month
    highest_month = monthly_expense.idxmax()
    highest_amount = monthly_expense.max()
    print(f"\n📈 Highest Spending Month: Month {highest_month} | ₹{highest_amount:,.0f}")
    
    return comparison


def payment_method_analysis(df):
    """
    Analyze payment method usage.
    
    Returns:
        pd.DataFrame: Payment method analysis
    """
    print("\n" + "="*60)
    print("💳 PAYMENT METHOD ANALYSIS")
    print("="*60)
    
    payment_stats = df.groupby('Payment Method').agg({
        'Amount': ['sum', 'count', 'mean']
    }).round(2)
    payment_stats.columns = ['Total', 'Count', 'Average']
    payment_stats = payment_stats.sort_values('Total', ascending=False)
    
    print("\n📊 Payment Method Usage:")
    print(payment_stats)
    
    # Percentage breakdown
    total = payment_stats['Count'].sum()
    print("\n📈 Payment Method Percentage:")
    for method, count in payment_stats['Count'].items():
        pct = (count / total * 100)
        print(f"   {method:15} : {pct:6.2f}%")
    
    return payment_stats


def weekday_analysis(df):
    """
    Analyze spending by day of week.
    
    Returns:
        pd.DataFrame: Weekday analysis
    """
    print("\n" + "="*60)
    print("📆 WEEKDAY ANALYSIS")
    print("="*60)
    
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
                     'Friday', 'Saturday', 'Sunday']
    
    weekday_stats = df.groupby('Weekday')['Amount'].agg([
        ('Total', 'sum'),
        ('Count', 'count'),
        ('Average', 'mean')
    ]).reindex(weekday_order).round(2)
    
    print("\n📊 Spending by Weekday:")
    print(weekday_stats)
    
    return weekday_stats


def income_expense_summary(df):
    """
    Generate overall income and expense summary.
    
    Returns:
        dict: Summary statistics
    """
    print("\n" + "="*60)
    print("💵 INCOME vs EXPENSE SUMMARY")
    print("="*60)
    
    total_income = df[df['Type'] == 'Income']['Amount'].sum()
    total_expense = df[df['Type'] == 'Expense']['Amount'].sum()
    net_savings = total_income - total_expense
    
    print(f"\n📊 Total Income:    ₹{total_income:>15,.0f}")
    print(f"📊 Total Expense:   ₹{total_expense:>15,.0f}")
    print(f"💰 Net Savings:     ₹{net_savings:>15,.0f}")
    
    if net_savings > 0:
        savings_pct = (net_savings / total_income * 100)
        print(f"✅ Savings Rate:    {savings_pct:>15.2f}%")
    else:
        overspend = abs(net_savings)
        overspend_pct = (overspend / total_income * 100)
        print(f"🔴 Overspent:       ₹{overspend:>15,.0f}")
        print(f"🔴 Overspend Rate:  {overspend_pct:>15.2f}%")
    
    summary = {
        'Total Income': total_income,
        'Total Expense': total_expense,
        'Net Savings': net_savings,
        'Savings Rate (%)': (net_savings / total_income * 100) if total_income > 0 else 0
    }
    
    return summary


def generate_all_analysis(input_path='data/cleaned_expenses.csv'):
    """
    Run all analysis modules.
    
    Args:
        input_path (str): Path to cleaned CSV file
    
    Returns:
        dict: Dictionary containing all analysis results
    """
    print("\n🚀 Starting Comprehensive EDA Analysis...\n")
    
    # Load data
    df = pd.read_csv(input_path)
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Run all analyses
    category_result = category_analysis(df)
    monthly_result = monthly_analysis(df)
    payment_result = payment_method_analysis(df)
    weekday_result = weekday_analysis(df)
    summary_result = income_expense_summary(df)
    
    print("\n" + "="*60)
    print("✨ EDA ANALYSIS COMPLETE!")
    print("="*60)
    
    return {
        'category': category_result,
        'monthly': monthly_result,
        'payment': payment_result,
        'weekday': weekday_result,
        'summary': summary_result
    }


if __name__ == "__main__":
    analysis_results = generate_all_analysis()