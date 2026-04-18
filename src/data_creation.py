"""
Data Creation Module
====================
This module generates synthetic expense data for the Expense Tracker App.

Functions:
- generate_synthetic_data(): Creates realistic expense transactions with dates, 
  categories, amounts, and payment methods.

Output:
- data/expenses.csv with 200+ transactions

Author: Your Name
Date: 2026-04-16
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

def generate_synthetic_data(n_records=200, output_path='data/expenses.csv'):
    """
    Generate synthetic expense data for simulation.
    
    Args:
        n_records (int): Number of expense records to generate (default: 200)
        output_path (str): Path to save the CSV file (default: 'data/expenses.csv')
    
    Returns:
        pd.DataFrame: DataFrame containing generated expense data
    
    Example:
        >>> df = generate_synthetic_data(300, 'data/expenses.csv')
        >>> print(df.head())
    """
    
    # Ensure data directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Define categories and payment methods
    expense_categories = ['Food', 'Transport', 'Rent', 'Entertainment', 
                         'Health', 'Shopping', 'Bills', 'Education']
    income_categories = ['Salary']
    all_categories = expense_categories + income_categories
    payment_methods = ['Card', 'UPI', 'Cash', 'Net Banking', 'Wallet']
    
    # Initialize data list
    data = []
    
    # Generate transactions
    for _ in range(n_records):
        # Random date within 2024
        month = random.randint(1, 12)
        day = random.randint(1, 28)  # Use 28 to avoid month-end issues
        date = f'2024-{month:02d}-{day:02d}'
        
        # 85% expenses, 15% income
        if random.random() < 0.15:
            # Income transaction
            transaction_type = 'Income'
            category = 'Salary'
            amount = random.randint(30000, 80000)
            payment_method = random.choice(['Net Banking', 'Card'])
            description = 'Monthly salary'
        else:
            # Expense transaction
            transaction_type = 'Expense'
            category = random.choice(expense_categories)
            payment_method = random.choice(payment_methods)
            
            # Amount varies by category
            if category == 'Rent':
                amount = random.randint(10000, 25000)
                description = 'Monthly rent'
            elif category == 'Food':
                amount = random.randint(100, 800)
                description = random.choice(['Lunch', 'Dinner', 'Groceries', 'Coffee'])
            elif category == 'Transport':
                amount = random.randint(50, 500)
                description = random.choice(['Uber', 'Auto', 'Petrol', 'Metro'])
            elif category == 'Bills':
                amount = random.randint(500, 3000)
                description = random.choice(['Electricity', 'Water', 'Internet'])
            elif category == 'Entertainment':
                amount = random.randint(200, 2000)
                description = random.choice(['Movie', 'Gaming', 'Streaming', 'Concert'])
            elif category == 'Health':
                amount = random.randint(300, 5000)
                description = random.choice(['Doctor', 'Medicine', 'Gym', 'Dental'])
            elif category == 'Shopping':
                amount = random.randint(500, 5000)
                description = random.choice(['Clothes', 'Books', 'Gadgets', 'Gifts'])
            else:  # Education
                amount = random.randint(2000, 10000)
                description = random.choice(['Tuition', 'Books', 'Course', 'Exam Fee'])
        
        # Append to data
        data.append({
            'Date': date,
            'Category': category,
            'Description': description,
            'Amount': amount,
            'Payment Method': payment_method,
            'Type': transaction_type
        })
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv(output_path, index=False)
    
    print("✅ Synthetic expense data generated successfully!")
    print(f"📊 Total Records: {len(df)}")
    print(f"💾 Saved to: {output_path}")
    print(f"\n📋 Data Preview:\n{df.head(10)}")
    print(f"\n📈 Summary:\n{df['Type'].value_counts()}")
    
    return df


if __name__ == "__main__":
    # Run data generation
    print("🚀 Starting Data Generation Module...\n")
    df = generate_synthetic_data(n_records=200)
    print("\n✨ Data generation complete!")