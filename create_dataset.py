
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

records = [
    ("2024-01", "Technology", 82000, 51000),
    ("2024-01", "Marketing", 42000, 29000),
    ("2024-01", "Operations", 55000, 41000),
    ("2024-02", "Technology", 85000, 52000),
    ("2024-02", "Marketing", 44000, 30000),
    ("2024-02", "Operations", 56000, 42000),
    ("2024-03", "Technology", 88000, 54000),
    ("2024-03", "Marketing", 46000, 31500),
    ("2024-03", "Operations", 58000, 43000),
    ("2024-04", "Technology", 90000, 55000),
    ("2024-04", "Marketing", 47000, 32000),
    ("2024-04", "Operations", 60000, 44500),
    ("2024-05", "Technology", 94000, 57000),
    ("2024-05", "Marketing", 49000, 33000),
    ("2024-05", "Operations", 61000, 45000),
    ("2024-06", "Technology", 97000, 59000),
    ("2024-06", "Marketing", 51000, 34500),
    ("2024-06", "Operations", 63000, 46000),
    ("2024-07", "Technology", 101000, 61000),
    ("2024-07", "Marketing", 53000, 35500),
    ("2024-07", "Operations", 65000, 47500),
    ("2024-08", "Technology", 103000, 62000),
    ("2024-08", "Marketing", 54000, 36000),
    ("2024-08", "Operations", 66000, 48000),
    ("2024-09", "Technology", 108000, 65000),
    ("2024-09", "Marketing", 56000, 37500),
    ("2024-09", "Operations", 68000, 49500),
    ("2024-10", "Technology", 112000, 67000),
    ("2024-10", "Marketing", 58000, 39000),
    ("2024-10", "Operations", 70000, 51000),
    ("2024-11", "Technology", 118000, 70000),
    ("2024-11", "Marketing", 61000, 40500),
    ("2024-11", "Operations", 73000, 53000),
    ("2024-12", "Technology", 125000, 74000),
    ("2024-12", "Marketing", 65000, 43000),
    ("2024-12", "Operations", 76000, 55000),
    ("2025-01", "Technology", 130000, 76000),
    ("2025-01", "Marketing", 67000, 44000),
    ("2025-01", "Operations", 78000, 56000),
    ("2025-02", "Technology", 134000, 78000),
    ("2025-02", "Marketing", 69000, 45500),
    ("2025-02", "Operations", 80000, 57500),
    ("2025-03", "Technology", 140000, 81000),
    ("2025-03", "Marketing", 72000, 47000),
    ("2025-03", "Operations", 83000, 59000),
    ("2025-04", "Technology", 145000, 83000),
    ("2025-04", "Marketing", 74000, 48000),
    ("2025-04", "Operations", 85000, 60500),
    ("2025-05", "Technology", 150000, 86000),
    ("2025-05", "Marketing", 77000, 50000),
    ("2025-05", "Operations", 88000, 62500),
    ("2025-06", "Technology", 157000, 89000),
    ("2025-06", "Marketing", 80000, 52000),
    ("2025-06", "Operations", 91000, 64500),
    ("2025-07", "Technology", 162000, 92000),
    ("2025-07", "Marketing", 82000, 53000),
    ("2025-07", "Operations", 93000, 66000),
    ("2025-08", "Technology", 168000, 95000),
    ("2025-08", "Marketing", 85000, 55000),
    ("2025-08", "Operations", 96000, 68000),
    ("2025-09", "Technology", 175000, 98000),
    ("2025-09", "Marketing", 88000, 57000),
    ("2025-09", "Operations", 99000, 70000),
    ("2025-10", "Technology", 182000, 102000),
    ("2025-10", "Marketing", 91000, 58500),
    ("2025-10", "Operations", 102000, 72000),
    ("2025-11", "Technology", 190000, 106000),
    ("2025-11", "Marketing", 95000, 61000),
    ("2025-11", "Operations", 106000, 74500),
    ("2025-12", "Technology", 200000, 110000),
    ("2025-12", "Marketing", 100000, 64000),
    ("2025-12", "Operations", 110000, 77000),
]

df = pd.DataFrame(
    records,
    columns=["Month", "Department", "Revenue", "Expenses"]
)

df["Month"] = pd.to_datetime(df["Month"], format="%Y-%m")
df["Profit"] = df["Revenue"] - df["Expenses"]
df["Profit Margin (%)"] = (
    df["Profit"] / df["Revenue"] * 100
).round(2)

output_path = DATA_DIR / "financial_data.csv"
df.to_csv(output_path, index=False)

print(f"Dataset created successfully: {output_path}")
print(f"Rows: {len(df)}")
print("\nPreview:")
print(df.head(9).to_string(index=False))
