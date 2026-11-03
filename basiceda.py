# %%

file_path=r"C:\Users\User\Downloads\sales_data_sample.csv"

import pandas as pd
import numpy as np



# LEVEL 0: Loading
df = pd.read_csv(
    file_path,
    encoding="cp1252"
)

# Preserve original data
raw_df = df.copy(deep=True)

# LEVEL 1: Structure
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.info())
print(df.head())
print(df.tail())
print(df.sample(5, random_state=42))

# Verify dataset grain
print("Rows:", len(df))
print("Orders:", df["ORDERNUMBER"].nunique())
print(
    "Duplicate order-line keys:",
    df.duplicated(
        subset=["ORDERNUMBER", "ORDERLINENUMBER"]
    ).sum()
)

# LEVEL 2: Cardinality and categories
cardinality = pd.DataFrame({
    "dtype": df.dtypes,
    "unique": df.nunique(),
    "unique_ratio": df.nunique() / len(df)
})

print(cardinality)

for col in ["STATUS", "PRODUCTLINE", "DEALSIZE"]:
    print(col)
    print(df[col].value_counts(dropna=False))
    print(
        df[col].value_counts(
            normalize=True,
            dropna=False
        ) * 100
    )

# LEVEL 3: Date conversion
converted_dates = pd.to_datetime(
    df["ORDERDATE"],
    format="%m/%d/%Y %H:%M",
    errors="coerce"
)

print(
    "Failed date conversions:",
    (df["ORDERDATE"].notna() &
     converted_dates.isna()).sum()
)

df["ORDERDATE"] = converted_dates

print(
    "Year mismatches:",
    (df["ORDERDATE"].dt.year != df["YEAR_ID"]).sum()
)

# LEVEL 4: Descriptive statistics
print(
    df[["SALES", "QUANTITYORDERED",
        "PRICEEACH", "MSRP"]].describe()
)

sales = df["SALES"]

print("Mean:", sales.mean())
print("Median:", sales.median())
print("Std:", sales.std())
print("Variance:", sales.var())
print("Range:", sales.max() - sales.min())

q1 = sales.quantile(0.25)
q3 = sales.quantile(0.75)

print("IQR:", q3 - q1)

# Diagnose arithmetic assumption
df["calculated_sales"] = (
    df["QUANTITYORDERED"] * df["PRICEEACH"]
)

sales_mismatch = (
    df["SALES"] - df["calculated_sales"]
).abs() > 0.01

print("Sales mismatches:", sales_mismatch.sum())

# LEVEL 5: Missing values
missing_report = pd.DataFrame({
    "missing_count": df.isna().sum(),
    "missing_pct": (df.isna().mean() * 100).round(2)
})

print(
    missing_report.sort_values(
        "missing_pct", ascending=False
    )
)

print(
    "Rows containing missing values:",
    df.isna().any(axis=1).sum()
)

print(
    "Rows remaining after dropna:",
    len(df.dropna())
)

# Diagnose country-based missingness
for col in ["TERRITORY", "STATE", "POSTALCODE"]:
    report = (
        df.groupby("COUNTRY")[col]
        .apply(lambda s: s.isna().mean() * 100)
        .sort_values(ascending=False)
    )
    print(f"\nMissingness by country: {col}")
    print(report)


# %%



