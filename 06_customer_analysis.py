
import pandas as pd
from pathlib import Path

# ==========================================
# 1. LOAD THE DATASET
# ==========================================

file_path = "data/raw/sample_-_superstore (1).xls"

df = pd.read_excel(file_path)

print("Dataset loaded successfully!")
print("Total records:", len(df))


# ==========================================
# 2. BASIC CUSTOMER INFORMATION
# ==========================================

print("\n========== CUSTOMER INFORMATION ==========")

print("Unique customers:", df["Customer ID"].nunique())
print("Unique customer names:", df["Customer Name"].nunique())
print("Unique orders:", df["Order ID"].nunique())


# ==========================================
# 3. CUSTOMER-WISE ANALYSIS
# ==========================================

customer_analysis = (
    df.groupby(["Customer ID", "Customer Name"])
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Orders=("Order ID", "nunique"),
        Total_Quantity=("Quantity", "sum")
    )
    .reset_index()
)

# Sort customers by sales
customer_analysis = customer_analysis.sort_values(
    by="Total_Sales",
    ascending=False
)


# ==========================================
# 4. TOP 10 CUSTOMERS BY SALES
# ==========================================

print("\n========== TOP 10 CUSTOMERS BY SALES ==========")

print(
    customer_analysis[
        ["Customer Name", "Total_Sales", "Total_Profit", "Total_Orders"]
    ].head(10).round(2).to_string(index=False)
)


# ==========================================
# 5. TOP 10 CUSTOMERS BY PROFIT
# ==========================================

top_profit_customers = customer_analysis.sort_values(
    by="Total_Profit",
    ascending=False
)

print("\n========== TOP 10 CUSTOMERS BY PROFIT ==========")

print(
    top_profit_customers[
        ["Customer Name", "Total_Sales", "Total_Profit", "Total_Orders"]
    ].head(10).round(2).to_string(index=False)
)


# ==========================================
# 6. BOTTOM 10 CUSTOMERS BY PROFIT
# ==========================================

bottom_profit_customers = customer_analysis.sort_values(
    by="Total_Profit",
    ascending=True
)

print("\n========== 10 CUSTOMERS WITH LOWEST PROFIT ==========")

print(
    bottom_profit_customers[
        ["Customer Name", "Total_Sales", "Total_Profit", "Total_Orders"]
    ].head(10).round(2).to_string(index=False)
)


# ==========================================
# 7. SAVE CUSTOMER ANALYSIS
# ==========================================

output_folder = Path("outputs")
output_folder.mkdir(parents=True, exist_ok=True)

output_path = output_folder / "customer_analysis.csv"

customer_analysis.to_csv(output_path, index=False)

print("\nCustomer analysis saved to:", output_path)


# ==========================================
# 8. BUSINESS INSIGHTS
# ==========================================

highest_sales_customer = customer_analysis.loc[
    customer_analysis["Total_Sales"].idxmax()
]

highest_profit_customer = customer_analysis.loc[
    customer_analysis["Total_Profit"].idxmax()
]

lowest_profit_customer = customer_analysis.loc[
    customer_analysis["Total_Profit"].idxmin()
]

print("\n========== CUSTOMER BUSINESS INSIGHTS ==========")

print("\nHighest-sales customer:")
print(highest_sales_customer["Customer Name"])
print("Total sales:", round(highest_sales_customer["Total_Sales"], 2))

print("\nHighest-profit customer:")
print(highest_profit_customer["Customer Name"])
print("Total profit:", round(highest_profit_customer["Total_Profit"], 2))

print("\nLowest-profit customer:")
print(lowest_profit_customer["Customer Name"])
print("Total profit:", round(lowest_profit_customer["Total_Profit"], 2))

print("\nCustomer analysis completed successfully!")
