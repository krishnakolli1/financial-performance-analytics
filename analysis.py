
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "financial_data.csv"
CHARTS_DIR = BASE_DIR / "charts"


def main():
    """Analyze financial performance across months and departments."""

    if not DATA_PATH.exists():
        print(f"Dataset not found: {DATA_PATH}")
        print("Run create_dataset.py first.")
        return

    CHARTS_DIR.mkdir(exist_ok=True)

    df = pd.read_csv(DATA_PATH, parse_dates=["Month"])

    # Validate and prepare data
    df = df.drop_duplicates()
    df = df.dropna(
        subset=["Month", "Department", "Revenue", "Expenses"]
    )

    df["Profit"] = df["Revenue"] - df["Expenses"]
    df["Profit Margin (%)"] = (
        df["Profit"] / df["Revenue"].replace(0, float("nan")) * 100
    )
    df["Year"] = df["Month"].dt.year

    # Overall financial KPIs
    total_revenue = df["Revenue"].sum()
    total_expenses = df["Expenses"].sum()
    total_profit = df["Profit"].sum()
    profit_margin = (
        total_profit / total_revenue * 100 if total_revenue else 0
    )

    print("\n" + "=" * 58)
    print("          FINANCIAL PERFORMANCE ANALYTICS")
    print("=" * 58)
    print(f"Total revenue:       ${total_revenue:,.2f}")
    print(f"Total expenses:      ${total_expenses:,.2f}")
    print(f"Total profit:        ${total_profit:,.2f}")
    print(f"Overall profit margin: {profit_margin:.2f}%")
    print(f"Departments:         {df['Department'].nunique()}")
    print(f"Months covered:      {df['Month'].nunique()}")

    # Performance by department
    department_summary = (
        df.groupby("Department")[["Revenue", "Expenses", "Profit"]]
        .sum()
        .sort_values("Revenue", ascending=False)
    )
    department_summary["Profit Margin (%)"] = (
        department_summary["Profit"]
        / department_summary["Revenue"] * 100
    )

    print("\nFinancial performance by department:")
    print(department_summary.round(2).to_string())

    # Monthly totals across departments
    monthly_summary = (
        df.groupby("Month")[["Revenue", "Expenses", "Profit"]]
        .sum()
        .sort_index()
    )

    print("\nLatest six months:")
    print(monthly_summary.tail(6).round(2).to_string())

    # Yearly comparison
    yearly_summary = (
        df.groupby("Year")[["Revenue", "Expenses", "Profit"]].sum()
    )
    yearly_summary["Profit Margin (%)"] = (
        yearly_summary["Profit"] / yearly_summary["Revenue"] * 100
    )

    print("\nYearly financial performance:")
    print(yearly_summary.round(2).to_string())

    # Chart 1: Monthly revenue and expenses
    ax = monthly_summary[["Revenue", "Expenses"]].plot(
        figsize=(12, 6), marker="o"
    )
    ax.set_title("Monthly Revenue vs. Expenses")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount ($)")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "monthly_revenue_expenses.png", dpi=150)
    plt.close()

    # Chart 2: Profit by department
    plt.figure(figsize=(9, 5))
    department_summary["Profit"].sort_values().plot(kind="barh")
    plt.title("Total Profit by Department")
    plt.xlabel("Profit ($)")
    plt.ylabel("Department")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "profit_by_department.png", dpi=150)
    plt.close()

    # Chart 3: Yearly revenue
    yearly_summary["Revenue"].plot(
        kind="bar", figsize=(8, 5)
    )
    plt.title("Yearly Revenue Comparison")
    plt.xlabel("Year")
    plt.ylabel("Revenue ($)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "yearly_revenue.png", dpi=150)
    plt.close()

    # Chart 4: Department profit margin
    plt.figure(figsize=(9, 5))
    department_summary["Profit Margin (%)"].sort_values().plot(
        kind="barh"
    )
    plt.title("Profit Margin by Department")
    plt.xlabel("Profit Margin (%)")
    plt.ylabel("Department")
    plt.tight_layout()
    plt.savefig(CHARTS_DIR / "profit_margin_by_department.png", dpi=150)
    plt.close()

    # Export reports
    department_summary.to_csv(
        CHARTS_DIR / "department_summary.csv"
    )
    monthly_summary.to_csv(CHARTS_DIR / "monthly_summary.csv")
    yearly_summary.to_csv(CHARTS_DIR / "yearly_summary.csv")

    print(f"\nCharts and reports saved to: {CHARTS_DIR}")
    print("Analysis completed successfully!")


if __name__ == "__main__":
    main()
