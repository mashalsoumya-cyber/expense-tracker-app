"""
Expense Tracker App - Complete Pipeline
========================================
This is the main executable script that runs the entire workflow:
1. Data Creation
2. Data Cleaning
3. EDA Analysis
4. Visualizations
5. Insights Generation

Run this single script to execute the entire project!

Usage:
    python main.py

Author: Your Name
Date: 2026-04-16
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import all modules
from data_creation import generate_synthetic_data
from data_cleaning import clean_expense_data
from eda_analysis import generate_all_analysis
from visualizations import save_all_visualizations
from insights_generator import generate_insights

def main():
    """
    Execute the complete Expense Tracker Pipeline.
    """
    
    print("\n" + "="*70)
    print("🚀 EXPENSE TRACKER APP - COMPLETE PIPELINE")
    print("="*70)
    
    # ===== PHASE 1: DATA CREATION =====
    print("\n\n📊 PHASE 1: DATA CREATION")
    print("-"*70)
    try:
        df_raw = generate_synthetic_data(n_records=200, output_path='data/expenses.csv')
        phase1_status = "✅ COMPLETE"
    except Exception as e:
        print(f"❌ ERROR in Phase 1: {str(e)}")
        phase1_status = "❌ FAILED"
        return
    
    # ===== PHASE 2: DATA CLEANING =====
    print("\n\n🧹 PHASE 2: DATA CLEANING & PREPROCESSING")
    print("-"*70)
    try:
        df_cleaned = clean_expense_data(
            input_path='data/expenses.csv',
            output_path='data/cleaned_expenses.csv'
        )
        phase2_status = "✅ COMPLETE"
    except Exception as e:
        print(f"❌ ERROR in Phase 2: {str(e)}")
        phase2_status = "❌ FAILED"
        return
    
    # ===== PHASE 3: EDA ANALYSIS =====
    print("\n\n🔍 PHASE 3: EXPLORATORY DATA ANALYSIS")
    print("-"*70)
    try:
        analysis_results = generate_all_analysis(input_path='data/cleaned_expenses.csv')
        phase3_status = "✅ COMPLETE"
    except Exception as e:
        print(f"❌ ERROR in Phase 3: {str(e)}")
        phase3_status = "❌ FAILED"
        return
    
    # ===== PHASE 4: VISUALIZATIONS =====
    print("\n\n🎨 PHASE 4: CREATING VISUALIZATIONS")
    print("-"*70)
    try:
        save_all_visualizations(input_path='data/cleaned_expenses.csv')
        phase4_status = "✅ COMPLETE"
    except Exception as e:
        print(f"❌ ERROR in Phase 4: {str(e)}")
        phase4_status = "❌ FAILED"
        return
    
    # ===== PHASE 5: INSIGHTS GENERATION =====
    print("\n\n💡 PHASE 5: GENERATING INSIGHTS")
    print("-"*70)
    try:
        insights = generate_insights(
            input_path='data/cleaned_expenses.csv',
            output_path='outputs/insights_report.txt'
        )
        phase5_status = "✅ COMPLETE"
    except Exception as e:
        print(f"❌ ERROR in Phase 5: {str(e)}")
        phase5_status = "❌ FAILED"
        return
    
    # ===== FINAL SUMMARY =====
    print("\n\n" + "="*70)
    print("📋 PIPELINE EXECUTION SUMMARY")
    print("="*70)
    print(f"\nPhase 1 - Data Creation:        {phase1_status}")
    print(f"Phase 2 - Data Cleaning:        {phase2_status}")
    print(f"Phase 3 - EDA Analysis:         {phase3_status}")
    print(f"Phase 4 - Visualizations:       {phase4_status}")
    print(f"Phase 5 - Insights Generation:  {phase5_status}")
    
    print("\n" + "="*70)
    print("📁 OUTPUT LOCATIONS:")
    print("="*70)
    print("\n   📊 Data Files:")
    print("      • data/expenses.csv")
    print("      • data/cleaned_expenses.csv")
    print("\n   📈 Visualizations:")
    print("      • outputs/01_category_total.png")
    print("      • outputs/02_category_pie.png")
    print("      • outputs/03_monthly_trend.png")
    print("      • outputs/04_weekday_count.png")
    print("      • outputs/05_income_expense_comparison.png")
    print("      • outputs/06_payment_method.png")
    print("\n   📄 Reports:")
    print("      • outputs/insights_report.txt")
    
    print("\n" + "="*70)
    print("✨ EXPENSE TRACKER APP - EXECUTION SUCCESSFUL!")
    print("="*70)
    print("\n🎉 Your project is ready for GitHub upload!\n")


if __name__ == "__main__":
    main()