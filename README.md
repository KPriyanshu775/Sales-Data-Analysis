# Sales Data Analysis Dashboard

An end-to-end data analysis project using Python, Pandas, Plotly and Streamlit to explore sales performance, profitability, customer behavior, product performance and regional trends.

## Project Overview

This project analyzes a Superstore sales dataset containing 10,194 records and 21 columns. It aims to identify business trends, evaluate profitability and provide actionable insights through data analysis and an interactive dashboard.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Streamlit
- Excel

## Key Features

- Dataset exploration and preprocessing
- Overall sales and profit analysis
- Regional and category performance analysis
- Monthly sales and profit trends
- Product performance analysis
- Customer profitability analysis
- Discount impact analysis
- Interactive dashboard with filters
- KPI metrics and visualizations
- Business insights and recommendations
- Filtered dataset export to CSV

## Dashboard Features

The Streamlit dashboard provides:
- Total Sales
- Total Profit
- Total Orders
- Unique Customers
- Profit Margin
- Monthly Sales and Profit Trends
- Regional Performance
- Category Performance
- Top 10 Products
- Business Insights
- Discount Impact Analysis
- Filtered Data Download

## Project Structure

```text
Sales-Data-Analysis/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── notebooks/
├── outputs/
├── dashboard/
├── report/
│
├── 01_data_understanding.py
├── 02_basic_sales_analysis.py
├── 03_regional_category_analysis.py
├── 04_time_series_analysis.py
├── 05_product_analysis.py
├── 06_customer_analysis.py
├── 07_business_insights.py
│
├── dashboard_app.py
├── requirements.txt
└── README.md
```

## Dataset Summary

- Total Records: 10,194
- Total Columns: 21
- Unique Customers: 804
- Unique Orders: 5,111
- Total Sales: $2,326,534.35
- Total Profit: $292,296.81
- Overall Profit Margin: 12.56%

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/KPriyanshu775/Sales-Data-Analysis.git
```

Navigate to the project folder:

```bash
cd Sales-Data-Analysis
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Place the dataset inside `data/raw/` with the filename:

`sample_-_superstore (1).xls`

Run the dashboard:

```bash
streamlit run dashboard_app.py
```

## Key Business Findings

- West region generated the highest sales and profit.
- Technology was the most profitable category.
- Tables, Bookcases and Supplies were loss-making subcategories.
- Sean Miller generated the highest customer sales.
- Tamara Chand generated the highest customer profit.
- Discount levels show different profitability outcomes that deserve further investigation.

## Author

Priyanshu Kumar

MCA Student | Lovely Professional University

GitHub: https://github.com/KPriyanshu775

## Project Purpose

Developed as a practical data analytics project to strengthen skills in Python programming, data cleaning, exploratory data analysis, visualization and interactive dashboard development.
