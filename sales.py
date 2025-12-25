# supermarket_sales_analysis.py
# -----------------------------------
# Author: Nisha Poojary
# Project: Supermarket Sales Analysis
# Description: Analyze supermarket sales dataset to extract business insights,
#              visualize sales trends, top products, branch performance, and customer insights.
# -----------------------------------

# -------------------------------
# Step 0: Import required libraries
# -------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style='whitegrid')

# -------------------------------
# Step 1: Load the dataset
# -------------------------------
file_path = 'supermarket_sales.csv'  # Update path if needed
df = pd.read_csv(file_path)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# -------------------------------
# Step 2: Initial Exploration
# -------------------------------
print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe())

print("\n--- First 5 Rows ---")
print(df.head())

# -------------------------------
# Step 3: Missing Values Check
# -------------------------------
print("\n--- Missing Values ---")
print(df.isnull().sum())

# -------------------------------
# Step 4: Key Visualizations
# -------------------------------

# 1. Total sales by branch
plt.figure(figsize=(8,5))
sns.barplot(x='Branch', y='Sales', data=df, estimator=sum, palette='viridis')
plt.title('Total Sales by Branch', fontsize=14)
plt.ylabel('Total Sales')
plt.xlabel('Branch')
plt.show()

# 2. Sales distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Sales'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Sales', fontsize=14)
plt.xlabel('Sales')
plt.show()

# 3. Payment method count
plt.figure(figsize=(8,5))
sns.countplot(x='Payment', data=df, palette='pastel')
plt.title('Number of Transactions by Payment Method', fontsize=14)
plt.show()

# 4. Quantity sold by product line
plt.figure(figsize=(10,6))
sns.barplot(x='Product line', y='Quantity', data=df, estimator=sum, palette='magma')
plt.title('Total Quantity Sold by Product Line', fontsize=14)
plt.xticks(rotation=45)
plt.show()

# 5. Branch vs Product Line Heatmap
branch_product = df.pivot_table(index='Branch', columns='Product line', values='Sales', aggfunc='sum')
plt.figure(figsize=(10,6))
sns.heatmap(branch_product, annot=True, fmt=".0f", cmap='YlGnBu')
plt.title('Branch vs Product Line Sales Heatmap', fontsize=14)
plt.show()

# 6. Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap', fontsize=14)
plt.show()

# -------------------------------
# Step 5: Insights
# -------------------------------

# Branch with highest sales
branch_sales = df.groupby('Branch')['Sales'].sum()
print("\n--- Branch with Highest Sales ---")
print(branch_sales)
print("🏆 Highest sales branch:", branch_sales.idxmax())

# Most popular product line
product_sales = df.groupby('Product line')['Quantity'].sum()
print("\n--- Most Popular Product Line ---")
print(product_sales)
print("⭐ Most sold product line:", product_sales.idxmax())

# Top 5 products by sales
top_products = df.groupby('Product line')['Sales'].sum().sort_values(ascending=False).head(5)
print("\n--- Top 5 Products by Sales ---")
print(top_products)

# Average sales per branch
print("\n--- Average Sales per Branch ---")
print(df.groupby('Branch')['Sales'].mean())

# Sales trend over time (monthly)
monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Sales'].sum()
plt.figure(figsize=(10,5))
monthly_sales.plot(kind='line', marker='o', color='green')
plt.title("Monthly Sales Trend", fontsize=14)
plt.ylabel("Sales")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.show()

# Customer type analysis
plt.figure(figsize=(8,5))
sns.barplot(x='Customer type', y='Sales', data=df, estimator=sum, palette='cool')
plt.title("Sales by Customer Type", fontsize=14)
plt.show()

# Gender-based analysis
plt.figure(figsize=(8,5))
sns.barplot(x='Gender', y='Sales', data=df, estimator=sum, palette='Set2')
plt.title("Sales by Gender", fontsize=14)
plt.show()

# Payment method sales distribution
payment_sales = df.groupby('Payment')['Sales'].sum()
plt.figure(figsize=(6,6))
payment_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
plt.title("Sales by Payment Method", fontsize=14)
plt.ylabel('')
plt.show()

# -------------------------------
# Step 6: Save Insights
# -------------------------------
branch_sales.to_csv('branch_sales_summary.csv')
product_sales.to_csv('product_sales_summary.csv')
top_products.to_csv('top_products_summary.csv')
monthly_sales.to_csv('monthly_sales_summary.csv')

print("\nInsights saved to CSV files.")
