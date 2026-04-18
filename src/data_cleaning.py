"""
Data Cleaning Module
====================
This module handles data validation, cleaning, and preprocessing.

Functions:
- clean_expense_data(): Removes duplicates, handles missing values, 
  standardizes formats, and creates derived features.

Output:
- data/cleaned_expenses.csv with cleaned and enriched data

Author: Your Name
Date: 2026-04-16
"""

import pandas as pd
import numpy as np
import os

def clean_expense_data(input_path='data/expenses.csv', 
                       output_path='data/cleaned_expenses.csv'):
    """
    Clean and preprocess expense data.
    
    Steps:
    1. Remove duplicate records
    2. Handle missing values
    3. Convert data types (Date, Amount)
    4. Standardize categorical values
    5. Create derived features (Month, Day, Weekday)
    
    Args:
        input_path (str): Path to raw CSV file
        output_path (str): Path to save cleaned CSV file
    
    Returns:
        pd.DataFrame: Cleaned and enriched DataFrame
    
    Example:
        >>> df_clean = clean_expense_data('data/expenses.csv', 'data/cleaned_expenses.csv')
        >>> print(df_clean.info())
    """
    
    print("🔍 Loading raw data...")
    df = pd.read_csv(input_path)
    original_count = len(df)
    print(f"📊 Original records: {original_count}")
    
    # --- STEP 1: Remove Duplicates ---
    print("\n🔄 Removing duplicates...")
    df = df.drop_duplicates()
    duplicates_removed = original_count - len(df)
    print(f"❌ Duplicates removed: {duplicates_removed}")
    
    # --- STEP 2: Check Missing Values ---
    print("\n❓ Checking for missing values...")
    missing = df.isnull().sum()
    print(missing[missing > 0] if missing.sum() > 0 else "✅ No missing values found!")
    
    # --- STEP 3: Handle Missing Values ---
    print("\n🛠️  Handling missing values...")
    df = df.dropna(subset=['Date', 'Amount', 'Category', 'Type'])
    print(f"✅ Rows after removing missing critical values: {len(df)}")
    
    # --- STEP 4: Convert Data Types ---
    print("\n📝 Converting data types...")
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    print("✅ Date and Amount converted to proper types")
    
    # --- STEP 5: Standardize Categorical Text ---
    print("\n🎯 Standardizing categorical values...")
    df['Category'] = df['Category'].astype(str).str.strip().str.title()
    df['Type'] = df['Type'].astype(str).str.strip().str.title()
    df['Payment Method'] = df['Payment Method'].astype(str).str.strip().str.title()
    df['Description'] = df['Description'].astype(str).str.strip().str.title()
    print("✅ Text standardized")
    
    # --- STEP 6: Create Derived Features ---
    print("\n➕ Creating derived features...")
    df['Month'] = df['Date'].dt.month_name()
    df['Month_Num'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['Weekday'] = df['Date'].dt.day_name()
    df['Year'] = df['Date'].dt.year
    print("✅ New columns added: Month, Month_Num, Day, Weekday, Year")
    
    # --- STEP 7: Sort by Date ---
    print("\n📅 Sorting by date...")
    df = df.sort_values('Date').reset_index(drop=True)
    
    # --- STEP 8: Save Cleaned Data ---
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\n💾 Cleaned data saved to: {output_path}")
    
    # --- STEP 9: Display Summary ---
    print("\n📊 Data Summary After Cleaning:")
    print(f"Total Records: {len(df)}")
    print(f"\n📋 Columns: {list(df.columns)}")
    print(f"\n📈 Data Info:")
    print(df.info())
    print(f"\n🔢 Sample Cleaned Data:")
    print(df.head(10))
    print(f"\n💡 Unique Categories: {df['Category'].unique()}")
    print(f"💡 Unique Payment Methods: {df['Payment Method'].unique()}")
    
    return df


if __name__ == "__main__":
    print("🚀 Starting Data Cleaning Module...\n")
    df_cleaned = clean_expense_data()
    print("\n✨ Data cleaning complete!")