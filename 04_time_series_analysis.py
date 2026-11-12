
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ==========================================
# 1. SET UP FILE PATHS
# ==========================================

file_path = "data/raw/sample_-_superstore (1).xls"

# Create the outputs folder if it does not exist
output_folder = Path("outputs")
output_folder.mkdir(parents=True, exist_ok=True)


# ==========================================
# 2. LOAD THE DATASET
# ==========================================

df = pd.read_excel(file_path)

print("\nDataset loaded successfully!")
print("Total rows:", len(df))
print("Total columns:", len(df.columns))


# ==========================================
# 3. PREPARE THE DATE COLUMN
# ==========================================

df["Order Date"] = pd.to_datetime(df["Order Date"])

# Extract year and month
df["Year-Month"] = df["Order Date"].dt.to_period("M")


# ==========================================
# 4. CALCULATE MONTHLY SALES AND PROFIT
# ==========================================

monthly_sales = df.groupby("Year-Month")["Sales"].sum()
monthly_profit = df.groupby("Year-Month")["Profit"].sum()


# ==========================================
# 5. DISPLAY MONTHLY SALES
# ==========================================

print("\n========== MONTHLY SALES ==========")
print(monthly_sales.round(2))

print("\nHighest Sales Month:")
print(monthly_sales.idxmax(), "-", round(monthly_sales.max(), 2))

print("\nLowest Sales Month:")
print(monthly_sales.idxmin(), "-", round(monthly_sales.min(), 2))


# ==========================================
# 6. DISPLAY MONTHLY PROFIT
# ==========================================

print("\n========== MONTHLY PROFIT ==========")
print(monthly_profit.round(2))

print("\nHighest Profit Month:")
print(monthly_profit.idxmax(), "-", round(monthly_profit.max(), 2))

print("\nLowest Profit Month:")
print(monthly_profit.idxmin(), "-", round(monthly_profit.min(), 2))


# ==========================================
# 7. PLOT MONTHLY SALES TREND
# ==========================================

plt.figure(figsize=(14, 6))

plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Trend", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Total Sales", fontsize=12)

plt.xticks(rotation=90)
plt.grid(True, alpha=0.4)
plt.tight_layout()

# Save the chart
sales_chart_path = output_folder / "monthly_sales_trend.png"
plt.savefig(sales_chart_path, dpi=300, bbox_inches="tight")

print("\nSales chart saved to:", sales_chart_path)

# Display the chart
plt.show()
plt.close()


# ==========================================
# 8. PLOT MONTHLY PROFIT TREND
# ==========================================

plt.figure(figsize=(14, 6))

plt.plot(
    monthly_profit.index.astype(str),
    monthly_profit.values,
    marker="o",
    linewidth=2
)

# Zero line helps identify loss-making months
plt.axhline(y=0, linestyle="--", linewidth=1)

plt.title("Monthly Profit Trend", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Total Profit", fontsize=12)

plt.xticks(rotation=90)
plt.grid(True, alpha=0.4)
plt.tight_layout()

# Save the chart
profit_chart_path = output_folder / "monthly_profit_trend.png"
plt.savefig(profit_chart_path, dpi=300, bbox_inches="tight")

print("Profit chart saved to:", profit_chart_path)

# Display the chart
plt.show()
plt.close()


# ==========================================
# 9. COMPLETION MESSAGE
# ==========================================

print("\n======================================")
print("TIME SERIES ANALYSIS COMPLETED!")
print("======================================")

print("Monthly sales chart:", sales_chart_path)
print("Monthly profit chart:", profit_chart_path)
