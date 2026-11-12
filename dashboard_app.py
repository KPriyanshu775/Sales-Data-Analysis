
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Sales Data Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Data Analysis Dashboard")
st.caption(
    "Explore sales, profitability, products and regional performance."
)

# ==========================================
# 2. LOAD DATASET
# ==========================================

@st.cache_data
def load_data():
    file_path = Path("data/raw/sample_-_superstore (1).xls")

    df = pd.read_excel(file_path)

    # Convert date columns into datetime format
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    # Handle mixed numeric and text postal codes
    if "Postal Code" in df.columns:
        df["Postal Code"] = df["Postal Code"].astype("string")

    return df


try:
    df = load_data()

except FileNotFoundError:
    st.error(
        "Dataset not found. Please check that the Excel file "
        "exists inside data/raw."
    )
    st.stop()

except Exception as error:
    st.error(f"Could not load the dataset: {error}")
    st.stop()


# ==========================================
# 3. SIDEBAR FILTERS
# ==========================================

st.sidebar.header("Dashboard Filters")

regions = sorted(df["Region"].dropna().unique())
categories = sorted(df["Category"].dropna().unique())

selected_regions = st.sidebar.multiselect(
    "Select Region",
    options=regions,
    default=regions
)

selected_categories = st.sidebar.multiselect(
    "Select Category",
    options=categories,
    default=categories
)

min_date = df["Order Date"].min().date()
max_date = df["Order Date"].max().date()

selected_dates = st.sidebar.date_input(
    "Select Order Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)


# ==========================================
# 4. APPLY FILTERS
# ==========================================

filtered_df = df[
    df["Region"].isin(selected_regions)
    & df["Category"].isin(selected_categories)
].copy()

if len(selected_dates) == 2:
    start_date, end_date = selected_dates

    filtered_df = filtered_df[
        filtered_df["Order Date"].dt.date.between(
            start_date,
            end_date
        )
    ]

if filtered_df.empty:
    st.warning("No records match your selected filters.")
    st.stop()


# ==========================================
# 5. KEY PERFORMANCE INDICATORS
# ==========================================

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()
total_customers = filtered_df["Customer ID"].nunique()

profit_margin = (
    total_profit / total_sales * 100
    if total_sales != 0
    else 0
)

st.subheader("Key Performance Indicators")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Total Orders", f"{total_orders:,}")
col4.metric("Unique Customers", f"{total_customers:,}")
col5.metric("Profit Margin", f"{profit_margin:.2f}%")


# ==========================================
# 6. MONTHLY SALES AND PROFIT
# ==========================================

st.subheader("Monthly Sales and Profit Trends")

monthly_df = filtered_df.copy()

monthly_df["Month"] = (
    monthly_df["Order Date"].dt.to_period("M").astype(str)
)

monthly_summary = (
    monthly_df.groupby("Month", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

monthly_long = monthly_summary.melt(
    id_vars="Month",
    value_vars=["Sales", "Profit"],
    var_name="Metric",
    value_name="Amount"
)

fig_monthly = px.line(
    monthly_long,
    x="Month",
    y="Amount",
    color="Metric",
    markers=True,
    title="Monthly Sales and Profit"
)

fig_monthly.update_layout(
    xaxis_title="Month",
    yaxis_title="Amount",
    hovermode="x unified"
)

st.plotly_chart(
    fig_monthly,
    width="stretch"
)


# ==========================================
# 7. REGIONAL PERFORMANCE
# ==========================================

st.subheader("Regional Performance")

region_summary = (
    filtered_df.groupby("Region", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

col1, col2 = st.columns(2)

with col1:

    fig_region_sales = px.bar(
        region_summary,
        x="Region",
        y="Sales",
        title="Sales by Region",
        text_auto=".2s"
    )

    st.plotly_chart(
        fig_region_sales,
        width="stretch"
    )


with col2:

    fig_region_profit = px.bar(
        region_summary,
        x="Region",
        y="Profit",
        title="Profit by Region",
        text_auto=".2s"
    )

    st.plotly_chart(
        fig_region_profit,
        width="stretch"
    )


# ==========================================
# 8. CATEGORY PERFORMANCE
# ==========================================

st.subheader("Category Performance")

category_summary = (
    filtered_df.groupby("Category", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
)

fig_category = px.bar(
    category_summary,
    x="Category",
    y="Sales",
    color="Profit",
    title="Category Sales and Profit",
    hover_data=["Quantity"]
)

st.plotly_chart(
    fig_category,
    width="stretch"
)


# ==========================================
# 9. TOP 10 PRODUCTS
# ==========================================

st.subheader("Top 10 Products by Sales")

product_summary = (
    filtered_df.groupby("Product Name", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
)

top_products = product_summary.nlargest(10, "Sales")

fig_products = px.bar(
    top_products.sort_values("Sales"),
    x="Sales",
    y="Product Name",
    orientation="h",
    color="Profit",
    title="Top 10 Products by Sales",
    hover_data=["Quantity"]
)

st.plotly_chart(
    fig_products,
    width="stretch"
)


# ==========================================
# 10. BUSINESS INSIGHTS & RECOMMENDATIONS
# ==========================================

st.divider()

st.subheader("💡 Business Insights & Recommendations")

# Highest sales and profit regions
best_sales_region = region_summary.loc[
    region_summary["Sales"].idxmax()
]

best_profit_region = region_summary.loc[
    region_summary["Profit"].idxmax()
]

# Most profitable category
best_category = category_summary.loc[
    category_summary["Profit"].idxmax()
]

# Best-selling product
best_product = product_summary.loc[
    product_summary["Sales"].idxmax()
]

# Find loss-making subcategories
subcategory_summary = (
    filtered_df.groupby("Sub-Category", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

loss_subcategories = (
    subcategory_summary[
        subcategory_summary["Profit"] < 0
    ]
    .sort_values("Profit")
)

# Display key insights
col1, col2 = st.columns(2)

with col1:
    st.markdown("**🏆 Highest Sales Region**")
    st.write(best_sales_region["Region"])
    st.metric(
        "Sales",
        f"${best_sales_region['Sales']:,.2f}"
    )

    st.markdown("**💰 Most Profitable Region**")
    st.write(best_profit_region["Region"])
    st.metric(
        "Profit",
        f"${best_profit_region['Profit']:,.2f}"
    )

with col2:
    st.markdown("**📦 Most Profitable Category**")
    st.write(best_category["Category"])
    st.metric(
        "Profit",
        f"${best_category['Profit']:,.2f}"
    )

    st.markdown("**⭐ Best-Selling Product**")
    st.write(best_product["Product Name"])
    st.metric(
        "Sales",
        f"${best_product['Sales']:,.2f}"
    )

# Loss-making subcategories
st.markdown("### ⚠️ Loss-Making Subcategories")

if not loss_subcategories.empty:
    st.dataframe(
        loss_subcategories,
        width="stretch"
    )
else:
    st.success("No loss-making subcategories found.")

# Business recommendations
st.markdown("### 📋 Business Recommendations")

if not loss_subcategories.empty:
    loss_names = ", ".join(
        loss_subcategories["Sub-Category"].astype(str)
    )

    st.write(
        f"1. Review pricing and discount strategies for "
        f"{loss_names}, as these subcategories are generating losses."
    )
else:
    st.write(
        "1. No subcategories are currently generating losses "
        "under the selected filters."
    )

st.write(
    f"2. Study the sales strategies of {best_sales_region['Region']} "
    "to identify practices that could work in other regions."
)

st.write(
    f"3. Analyze the success of {best_product['Product Name']} "
    "to identify opportunities for similar products."
)


# ==========================================
# DISCOUNT IMPACT ANALYSIS
# ==========================================

st.divider()

st.subheader("🏷️ Discount Impact Analysis")

discount_summary = (
    filtered_df.groupby("Discount", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Average_Profit=("Profit", "mean"),
        Orders=("Order ID", "nunique")
    )
    .sort_values("Discount")
)

# Identify highest and lowest profit discount levels
best_discount = discount_summary.loc[
    discount_summary["Profit"].idxmax()
]

worst_discount = discount_summary.loc[
    discount_summary["Profit"].idxmin()
]

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Highest-Profit Discount Level",
        f"{best_discount['Discount']:.0%}",
        f"${best_discount['Profit']:,.2f} profit"
    )

with col2:
    st.metric(
        "Lowest-Profit Discount Level",
        f"{worst_discount['Discount']:.0%}",
        f"${worst_discount['Profit']:,.2f} profit"
    )

# Profit by discount chart
fig_discount = px.bar(
    discount_summary,
    x="Discount",
    y="Profit",
    color="Profit",
    title="Total Profit by Discount Level",
    hover_data=["Sales", "Average_Profit", "Orders"],
    labels={
        "Discount": "Discount Rate",
        "Profit": "Total Profit"
    }
)

fig_discount.update_xaxes(tickformat=".0%")

st.plotly_chart(
    fig_discount,
    width="stretch"
)

st.info(
    "Business Note: Compare discount levels with profitability "
    "before changing pricing strategies. This relationship alone "
    "does not prove that discounts cause lower profits."
)


# ==========================================
# 10. RAW DATA TABLE
# ==========================================

with st.expander("View Filtered Dataset"):

    st.dataframe(
        filtered_df,
        width="stretch"
    )

    csv_data = filtered_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download Filtered Data as CSV",
        data=csv_data,
        file_name="filtered_sales_data.csv",
        mime="text/csv"
    )


# ==========================================
# 11. FOOTER
# ==========================================

st.divider()

st.caption(
    "Sales Data Analysis Dashboard | "
    "Built with Python, Pandas, Plotly and Streamlit"
)

st.success("Dashboard loaded successfully!")
