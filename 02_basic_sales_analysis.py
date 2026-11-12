import pandas as pd
from pathlib import Path

# Load the sales dataset
file_path = Path("data/raw/sample_-_superstore (1).xls")
df = pd.read_excel(file_path)

# Calculate basic sales metrics
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

# Display the results
print("\n========== SALES SUMMARY ==========")

print(f"Total Sales: {total_sales:,.2f}")
print(f"Total Profit: {total_profit:,.2f}")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Total Unique Orders: {total_orders:,}")
print(f"Total Unique Customers: {total_customers:,}")

print("\n========== PROFITABILITY ==========")

if total_sales != 0:
    profit_margin = (total_profit / total_sales) * 100
    print(f"Overall Profit Margin: {profit_margin:.2f}%")
else:
    print("Profit margin cannot be calculated because sales are zero.")