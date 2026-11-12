
import pandas as pd

# ==========================================
# 1. LOAD THE DATASET
# ==========================================

file_path = "data/raw/sample_-_superstore (1).xls"

df = pd.read_excel(file_path)

print("Dataset loaded successfully!")
print("Total records:", len(df))


# ==========================================
# 2. CHECK PRODUCT INFORMATION
# ==========================================

print("\n========== PRODUCT INFORMATION ==========")

print("Unique products:", df["Product Name"].nunique())
print("Unique product subcategories:", df["Sub-Category"].nunique())
print("Unique categories:", df["Category"].nunique())


# ==========================================
# 3. ANALYZE SALES AND PROFIT BY PRODUCT
# ==========================================

product_analysis = (
    df.groupby("Product Name")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum"),
        Total_Orders=("Order ID", "nunique")
    )
    .reset_index()
)

product_analysis = product_analysis.sort_values(
    by="Total_Sales",
    ascending=False
)


# ==========================================
# 4. TOP 10 PRODUCTS BY SALES
# ==========================================

print("\n========== TOP 10 PRODUCTS BY SALES ==========")

print(
    product_analysis[
        ["Product Name", "Total_Sales", "Total_Profit"]
    ].head(10).round(2).to_string(index=False)
)


# ==========================================
# 5. TOP 10 PRODUCTS BY PROFIT
# ==========================================

top_profit_products = product_analysis.sort_values(
    by="Total_Profit",
    ascending=False
)

print("\n========== TOP 10 PRODUCTS BY PROFIT ==========")

print(
    top_profit_products[
        ["Product Name", "Total_Sales", "Total_Profit"]
    ].head(10).round(2).to_string(index=False)
)


# ==========================================
# 6. BOTTOM 10 PRODUCTS BY PROFIT
# ==========================================

bottom_profit_products = product_analysis.sort_values(
    by="Total_Profit",
    ascending=True
)

print("\n========== 10 PRODUCTS WITH LOWEST PROFIT ==========")

print(
    bottom_profit_products[
        ["Product Name", "Total_Sales", "Total_Profit"]
    ].head(10).round(2).to_string(index=False)
)


# ==========================================
# 7. SAVE PRODUCT ANALYSIS
# ==========================================

output_path = "outputs/product_performance_analysis.csv"

product_analysis.to_csv(output_path, index=False)

print("\nProduct analysis saved to:", output_path)


# ==========================================
# 8. BUSINESS INSIGHTS
# ==========================================

best_sales_product = product_analysis.loc[
    product_analysis["Total_Sales"].idxmax()
]

best_profit_product = product_analysis.loc[
    product_analysis["Total_Profit"].idxmax()
]

worst_profit_product = product_analysis.loc[
    product_analysis["Total_Profit"].idxmin()
]

print("\n========== BUSINESS INSIGHTS ==========")

print(
    "Highest-sales product:",
    best_sales_product["Product Name"]
)

print(
    "Highest-sales product revenue:",
    round(best_sales_product["Total_Sales"], 2)
)

print(
    "\nHighest-profit product:",
    best_profit_product["Product Name"]
)

print(
    "Highest-profit product profit:",
    round(best_profit_product["Total_Profit"], 2)
)

print(
    "\nLowest-profit product:",
    worst_profit_product["Product Name"]
)

print(
    "Lowest-profit product profit:",
    round(worst_profit_product["Total_Profit"], 2)
)

print("\nProduct performance analysis completed successfully!")
