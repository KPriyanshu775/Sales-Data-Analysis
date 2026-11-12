import pandas as pd

# Load the sales dataset
file_path = "data/raw/sample_-_superstore (1).xls"
df = pd.read_excel(file_path)

# Sales and profit by region
print("\n========== SALES BY REGION ==========")

region_analysis = df.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
).round(2)

print(region_analysis.sort_values("Total_Sales", ascending=False))

# Sales and profit by category
print("\n========== SALES BY CATEGORY ==========")

category_analysis = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
).round(2)

print(category_analysis.sort_values("Total_Sales", ascending=False))

# Sales and profit by sub-category
print("\n========== SALES BY SUB-CATEGORY ==========")

subcategory_analysis = df.groupby("Sub-Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
).round(2)

print(subcategory_analysis.sort_values("Total_Sales", ascending=False))

# Regional performance
print("\n========== REGIONAL PERFORMANCE ==========")

print("Highest-sales region:", region_analysis["Total_Sales"].idxmax())
print("Lowest-sales region:", region_analysis["Total_Sales"].idxmin())
print("Highest-sales category:", category_analysis["Total_Sales"].idxmax())