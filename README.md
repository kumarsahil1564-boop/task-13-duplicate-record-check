# Task 13 – Duplicate Record Check

## Data Analytics Internship

This project checks a retail sales dataset for duplicate records and prepares a clean copy for further analysis.

### Objective
- Find exact duplicate records.
- Check duplicate Order IDs.
- Document duplicate entries.
- Remove confirmed exact duplicates.
- Prepare a cleaned dataset.
- Keep the cleaning process transparent with an audit note.

### Tools Used
- Excel
- Python
- Pandas
- CSV

### Results
- Original records: **24**
- Exact duplicate rows: **4**
- Duplicate groups: **2**
- Duplicate Order IDs: **RS1004 and RS1020**
- Cleaned records: **22**

### Method
1. Load the retail sales data.
2. Check complete rows for exact duplicates.
3. Check `Order_ID` for repeated identifiers.
4. Review repeated records before deletion.
5. Remove only confirmed exact duplicates.
6. Save the duplicate report and cleaned dataset.

### Audit Note
A repeated Order ID is not automatically treated as an error. If other business values are different, the record should be reviewed before deletion. In this task, only exact duplicate rows were removed.

### Files
- `retail_sales.csv` – original sample dataset
- `duplicate_report.csv` – exact duplicate records
- `cleaned_retail_sales.csv` – cleaned dataset
- `duplicate_check.py` – Pandas script
- `Task_13_Duplicate_Record_Check_Humanized.pdf` – project report

### Interview Questions
**What is a duplicate row?**  
A duplicate row is a record that repeats the same information as another record across the selected columns.

**How can duplicates affect totals?**  
Duplicates can cause the same transaction to be counted more than once, which can inflate sales, quantity, and transaction counts.

### Conclusion
The dataset was checked for duplicate records and the confirmed exact duplicates were removed. The cleaned dataset is now more suitable for further analysis and reporting.

**Prepared by: Sahil Kumar**
