import pandas as pd

# Load the raw retail-sales dataset
df = pd.read_csv("retail_sales.csv")

# Find complete rows that are exact duplicates
duplicates = df[df.duplicated(keep=False)]
duplicates.to_csv("duplicate_report.csv", index=False)

# Remove only exact duplicates
cleaned_df = df.drop_duplicates().reset_index(drop=True)
cleaned_df.to_csv("cleaned_retail_sales.csv", index=False)

print("Original records:", len(df))
print("Exact duplicate rows:", len(duplicates))
print("Cleaned records:", len(cleaned_df))
