# Financial Performance Analytics

## Project Overview
This project analyzes sample financial data across Technology, Marketing, and Operations departments over 24 months, from January 2024 to December 2025.

The goal is to evaluate revenue, expenses, profit, and profit margins to identify financial trends and compare department performance.

**Note:** This project uses a synthetic dataset created for learning and demonstration purposes.

## Tools and Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- CSV data analysis

## Key Performance Indicators
- **Total Revenue:** $6,624,000
- **Total Expenses:** $4,232,500
- **Total Profit:** $2,391,500
- **Overall Profit Margin:** 36.10%
- **Analysis Period:** January 2024 – December 2025

## Key Findings
1. Technology generated the highest revenue and profit among the three departments.
2. Total revenue increased from $2.6 million in 2024 to $4.024 million in 2025.
3. Total profit increased from $886,000 in 2024 to $1,505,500 in 2025.
4. Overall profit margin improved from 34.08% in 2024 to 37.41% in 2025.
5. Monthly revenue and profit increased during the final six months of 2025.

## Project Structure
```text
financial-performance-analytics/
├── data/
│   └── financial_data.csv
├── charts/
│   ├── monthly_revenue_expenses.png
│   ├── profit_by_department.png
│   ├── yearly_revenue.png
│   └── profit_margin_by_department.png
├── create_dataset.py
├── analysis.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run
1. Clone or download this repository.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Generate the sample dataset:
   ```bash
   python create_dataset.py
   ```
4. Run the analysis:
   ```bash
   python analysis.py
   ```

The script generates financial charts and CSV summary reports in the `charts/` folder.

## Skills Demonstrated
- Data cleaning and preprocessing
- Financial KPI calculations
- Department-level performance analysis
- Monthly and yearly trend analysis
- Data visualization
- Generating CSV reports using Python

## Disclaimer
The dataset is synthetic and does not represent the financial performance of an actual company.
