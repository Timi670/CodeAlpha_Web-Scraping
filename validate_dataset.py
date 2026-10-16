
import pandas as pd

print("Starting dataset validation...")

# Load the scraped data
df = pd.read_csv("books_data.csv")

print("\n===== DATASET OVERVIEW =====")
print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))
print("Column names:", df.columns.tolist())

print("\n===== FIRST 5 ROWS =====")
print(df.head().to_string(index=False))

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print("Duplicate rows:", df.duplicated().sum())

print("\n===== PRICE SUMMARY =====")
print(df["price_gbp"].describe())

print("\n===== RATING COUNTS =====")
print(df["rating"].value_counts(dropna=False))

print("\n===== QUALITY CHECKS =====")
print("Blank titles:", df["title"].isna().sum())
print("Missing prices:", df["price_gbp"].isna().sum())
print("Missing product URLs:", df["product_url"].isna().sum())

print("\nDataset validation completed!")
