"""
Insights Generator Module
==========================
This module generates actionable insights and recommendations from expense data.

Functions:
- generate_insights(): Creates comprehensive insights from analysis
- generate_report(): Creates a text report with findings

Output:
- Console insights and recommendation text file

Author: Your Name
Date: 2026-04-16
"""

import pandas as pd
from datetime import datetime

def generate_insights(input_path='data/cleaned_expenses.csv', 
                     output_path='outputs/insights_report.txt'):
    """
    Generate comprehensive insights from expense data.
    
    Args:
        input_path (str): Path to cleaned CSV file
        output_path (str): Path to save insights report
    
    Returns:
        dict: Dictionary containing all insights
    """
    print("\n" + "="*70)
    print("💡 GENERATING INSIGHTS FROM EXPENSE DATA")
    print("="*70)
    
    # Load data
    df = pd.read_csv(input_path)
    df['Date'] = pd.to_datetime(df['Date'])
    
    insights = {}
    
    # ===== INSIGHT 1: Income vs Expense =====
    total_income = df[df['Type'] == 'Income']['Amount'].sum()
    total_expense = df[df['Type'] == 'Expense']['Amount'].sum()
    net_savings = total_income - total_expense
    
    print(f"\n💰 FINANCIAL OVERVIEW:")
    print(f"   Total Income:  ₹{total_income:>12,.0f}")
    print(f"   Total Expense: ₹{total_expense:>12,.0f}")
    print(f"   Net Savings:   ₹{net_savings:>12,.0f}")
    
    if net_savings > 0:
        savings_rate = (net_savings / total_income * 100)
        print(f"   ✅ Savings Rate: {savings_rate:.2f}%")
        insights['financial_status'] = 'HEALTHY'
    else:
        print(f"   ⚠️  ALERT: Overspending detected!")
        insights['financial_status'] = 'OVERSPENDING'
    
    # ===== INSIGHT 2: Top Spending Categories =====
    print(f"\n🏆 TOP SPENDING CATEGORIES:")
    expense_df = df[df['Type'] == 'Expense']
    category_spend = expense_df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    
    insights['top_categories'] = category_spend.head(3).to_dict()
    
    for i, (cat, amount) in enumerate(category_spend.head(3).items(), 1):
        pct = (amount / category_spend.sum() * 100)
        print(f"   {i}. {cat:15} : ₹{amount:>10,.0f} ({pct:5.1f}%)")
    
    # ===== INSIGHT 3: Highest Spending Month =====
    print(f"\n📅 MONTHLY SPENDING ANALYSIS:")
    monthly_expense = df[df['Type'] == 'Expense'].groupby(df['Date'].dt.month)['Amount'].sum()
    highest_month = monthly_expense.idxmax()
    highest_amount = monthly_expense.max()
    
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    print(f"   Highest Spending: {month_names[highest_month-1]} | ₹{highest_amount:,.0f}")
    insights['highest_spending_month'] = (month_names[highest_month-1], highest_amount)
    
    # ===== INSIGHT 4: Overspending Months =====
    monthly_income = df[df['Type'] == 'Income'].groupby(df['Date'].dt.month)['Amount'].sum()
    overspent = []
    
    for month in monthly_expense.index:
        if month in monthly_income.index:
            if monthly_expense[month] > monthly_income[month]:
                diff = monthly_expense[month] - monthly_income[month]
                overspent.append((month_names[month-1], diff))
    
    if overspent:
        print(f"\n🔴 OVERSPENT MONTHS:")
        for month, diff in overspent:
            print(f"   ⚠️  {month}: Overspent by ₹{diff:,.0f}")
        insights['overspent_months'] = overspent
    else:
        print(f"\n✅ No overspent months detected!")
        insights['overspent_months'] = []
    
    # ===== INSIGHT 5: Average Daily Spending =====
    total_days = (df['Date'].max() - df['Date'].min()).days + 1
    avg_daily_expense = total_expense / total_days
    
    print(f"\n📊 DAILY SPENDING METRICS:")
    print(f"   Average Daily Expense: ₹{avg_daily_expense:,.0f}")
    print(f"   Average Daily Income:  ₹{total_income/total_days:,.0f}")
    insights['avg_daily_expense'] = avg_daily_expense
    
    # ===== INSIGHT 6: Most Used Payment Method =====
    print(f"\n💳 PAYMENT METHOD PREFERENCES:")
    payment_method_count = df['Payment Method'].value_counts()
    top_payment = payment_method_count.index[0]
    top_count = payment_method_count.iloc[0]
    pct = (top_count / len(df) * 100)
    
    print(f"   Most Used: {top_payment} ({top_count} transactions, {pct:.1f}%)")
    insights['top_payment_method'] = (top_payment, top_count)
    
    # ===== INSIGHT 7: Recommendations =====
    print(f"\n💡 RECOMMENDATIONS:")
    recommendations = []
    
    if net_savings < 0:
        rec = "🔴 Your expenses exceed income. Consider reducing discretionary spending."
        print(f"   1. {rec}")
        recommendations.append(rec)
    
    if category_spend.iloc[0] > total_expense * 0.4:
        top_cat = category_spend.index[0]
        rec = f"⚠️  {top_cat} is {(category_spend.iloc[0]/category_spend.sum()*100):.1f}% of expenses. Consider reviewing this category."
        print(f"   2. {rec}")
        recommendations.append(rec)
    
    if len(overspent) > 0:
        rec = "📍 Track monthly budgets more carefully to avoid overspending."
        print(f"   3. {rec}")
        recommendations.append(rec)
    
    if avg_daily_expense > (total_income / total_days) * 0.8:
        rec = "💰 Save at least 20% of your income for emergencies."
        print(f"   4. {rec}")
        recommendations.append(rec)
    
    insights['recommendations'] = recommendations
    
    # ===== INSIGHT 8: Spending Consistency =====
    print(f"\n📈 SPENDING CONSISTENCY:")
    expense_std = df[df['Type'] == 'Expense'].groupby(df['Date'].dt.month)['Amount'].sum().std()
    expense_mean = monthly_expense.mean()
    variance = (expense_std / expense_mean * 100) if expense_mean > 0 else 0
    
    print(f"   Monthly Variance: {variance:.1f}%")
    if variance < 20:
        print(f"   ✅ Your spending is consistent and predictable")
        insights['spending_consistency'] = 'CONSISTENT'
    elif variance < 40:
        print(f"   ⚠️  Moderate variation in monthly spending")
        insights['spending_consistency'] = 'MODERATE'
    else:
        print(f"   🔴 High variation in monthly spending")
        insights['spending_consistency'] = 'VOLATILE'
    
    # ===== Save Report to File =====
    save_insights_report(insights, output_path, df)
    
    print("\n" + "="*70)
    print("✨ Insights generation complete!")
    print(f"📄 Report saved to: {output_path}")
    print("="*70 + "\n")
    
    return insights


def save_insights_report(insights, output_path, df):
    """
    Save insights to a text report file.
    
    Args:
        insights (dict): Dictionary of insights
        output_path (str): Path to save report
        df (pd.DataFrame): Original dataframe
    """
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w') as f:
        f.write("="*70 + "\n")
        f.write("EXPENSE TRACKER - INSIGHTS REPORT\n")
        f.write("="*70 + "\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Data Period: {df['Date'].min().date()} to {df['Date'].max().date()}\n\n")
        
        f.write("-"*70 + "\n")
        f.write("FINANCIAL OVERVIEW\n")
        f.write("-"*70 + "\n")
        f.write(f"Financial Status: {insights['financial_status']}\n")
        f.write(f"Average Daily Expense: ₹{insights['avg_daily_expense']:,.0f}\n\n")
        
        f.write("-"*70 + "\n")
        f.write("TOP SPENDING CATEGORIES\n")
        f.write("-"*70 + "\n")
        for cat, amount in insights['top_categories'].items():
            f.write(f"{cat}: ₹{amount:,.0f}\n")
        f.write("\n")
        
        f.write("-"*70 + "\n")
        f.write("SPENDING CONSISTENCY\n")
        f.write("-"*70 + "\n")
        f.write(f"Status: {insights['spending_consistency']}\n\n")
        
        f.write("-"*70 + "\n")
        f.write("RECOMMENDATIONS\n")
        f.write("-"*70 + "\n")
        for i, rec in enumerate(insights['recommendations'], 1):
            f.write(f"{i}. {rec}\n")
        f.write("\n")
        
        f.write("="*70 + "\n")


if __name__ == "__main__":
    insights = generate_insights()