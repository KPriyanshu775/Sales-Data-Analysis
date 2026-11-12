
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ==========================================
# 1. LOAD DATASET
# ==========================================

file_path = "data/raw/sample_-_superstore (1).xls"

df = pd.read_excel(file_path)

output_folder = Path("outputs")
output_folder.mkdir(parents=True, exist_ok=True)

print("Dataset loaded successfully!")
print("Total records:", len(df))


# ==========================================
# 2. SALES AND PROFIT BY REGION
# ==========================================

region_analysis = (
    df.groupby("Region")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\n========== REGIONAL PERFORMANCE ==========")
print(region_analysis.round(2))


# ==========================================
# 3. SALES AND PROFIT BY CATEGORY
# ==========================================

category_analysis = (
    df.groupby("Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("\n========== CATEGORY PERFORMANCE ==========")
print(category_analysis.round(2))


# ==========================================
# 4. ANALYZE DISCOUNT AND PROFIT
# ==========================================

discount_analysis = (
    df.groupby("Discount")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Records=("Profit", "count")
    )
    .sort_index()
)

print("\n========== DISCOUNT ANALYSIS ==========")
print(discount_analysis.round(2))


# ==========================================
# 5. CHART: SALES BY REGION
# ==========================================

plt.figure(figsize=(9, 5))

region_analysis["Total_Sales"].plot(kind="bar")

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    output_folder / "sales_by_region.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ==========================================
# 6. CHART: PROFIT BY CATEGORY
# ==========================================

plt.figure(figsize=(9, 5))

category_analysis["Total_Profit"].plot(kind="bar")

plt.title("Total Profit by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    output_folder / "profit_by_category.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ==========================================
# 7. CHART: DISCOUNT VS PROFIT
# ==========================================

plt.figure(figsize=(9, 5))

plt.plot(
    discount_analysis.index,
    discount_analysis["Total_Profit"],
    marker="o"
)

plt.title("Discount vs Total Profit")
plt.xlabel("Discount")
plt.ylabel("Total Profit")
plt.grid(True, alpha=0.4)
plt.tight_layout()

plt.savefig(
    output_folder / "discount_vs_profit.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# ==========================================
# 8. SAVE ANALYSIS TABLES
# ==========================================

region_analysis.to_csv(
    output_folder / "regional_business_analysis.csv"
)

category_analysis.to_csv(
    output_folder / "category_business_analysis.csv"
)

discount_analysis.to_csv(
    output_folder / "discount_business_analysis.csv"
)


# ==========================================
# 9. DISPLAY BUSINESS INSIGHTS
# ==========================================

best_region = region_analysis["Total_Sales"].idxmax()
lowest_region = region_analysis["Total_Sales"].idxmin()

best_category = category_analysis["Total_Profit"].idxmax()
lowest_category = category_analysis["Total_Profit"].idxmin()

print("\n========== KEY BUSINESS INSIGHTS ==========")

print(
    f"Region with highest sales: {best_region} "
    f"(${region_analysis.loc[best_region, 'Total_Sales']:,.2f})"
)

print(
    f"Region with lowest sales: {lowest_region} "
    f"(${region_analysis.loc[lowest_region, 'Total_Sales']:,.2f})"
)

print(
    f"Most profitable category: {best_category} "
    f"(${category_analysis.loc[best_category, 'Total_Profit']:,.2f})"
)

print(
    f"Least profitable category: {lowest_category} "
    f"(${category_analysis.loc[lowest_category, 'Total_Profit']:,.2f})"
)

print("\nBusiness insights analysis completed successfully!")
print("Charts and CSV files saved in the outputs folder.")
