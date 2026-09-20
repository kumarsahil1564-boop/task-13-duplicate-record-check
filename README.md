# Task 13 – Duplicate Record Check

## Data Analytics Internship

This project focuses on finding duplicate records in a retail sales dataset and preparing a clean copy for further analysis.

## Objective

The main objective of this task is to:

- Find duplicate records
- Document the duplicate entries
- Check duplicate Order IDs
- Remove confirmed exact duplicates
- Prepare a cleaned dataset
- Maintain an audit note

## Tools Used

- Excel
- Python
- Pandas
- CSV

## Methodology

1. Loaded the retail sales dataset.
2. Checked complete rows for exact duplicates.
3. Checked the `Order_ID` column for repeated IDs.
4. Reviewed the duplicate records.
5. Removed only exact duplicate rows.
6. Prepared a cleaned copy of the dataset.

## Results

- Original records: **24**
- Exact duplicate rows: **4**
- Duplicate groups: **2**
- Duplicate Order IDs: **RS1004 and RS1020**
- Cleaned records: **22**

## Audit Note

I removed only the records that were completely identical. A repeated Order ID was not treated as an error automatically because different transactions can sometimes share an identifier and should be reviewed before deletion.

## Interview Questions

### What is a duplicate row?

A duplicate row is a record that contains the same information as another record across the selected columns.

### How can duplicates affect totals?

Duplicates can cause the same transaction to be counted more than once. This can increase sales totals, quantities, and transaction counts incorrectly.

## Conclusion

The dataset was checked for duplicate records and the confirmed exact duplicates were removed. The cleaned dataset is now more suitable for further analysis and reporting.

**Prepared by: Sahil Kumar**
