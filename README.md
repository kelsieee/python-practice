# csv_cleaner.py
A small Python script that cleans a CSV of support tickets. 
# What it does
1. Trims whitespace from every value and from the header names.
2. Removes blank rows, meaning rows that are empty after trimming (for example ,,,,).
3. Removes duplicates. Trimming happens first, so " Alice Tan " and "Alice Tan" count as the same value. The first occurrence is kept and the original row order is preserved.
4. Writes the cleaned CSV and prints a summary.

# Requirements
Python 3.6 or newer
No extra packages (standard library only)

# Usage
python csv_cleaner.py INPUT.csv [--ignore-case]

# Example
Input (tickets.csv):
ticket_id,customer,subject,status,priority
1001, Alice Tan ,Cannot log in,Open,High
1002,Bob Lee,  Report not printing,Closed,Low
1001, Alice Tan ,Cannot log in,Open,High
1003,Carol Ng,Email token not resolving  ,Open,Medium
 1003 ,Carol Ng,Email token not resolving,Open,Medium
,,,,
1004,Dan Wong,Slow query on PO screen,Open,High

Command: 
python csv_cleaner.py tickets.csv

Output (tickets_cleaned.csv):
ticket_id,customer,subject,status,priority
1001,Alice Tan,Cannot log in,Open,High
1002,Bob Lee,Report not printing,Closed,Low
1003,Carol Ng,Email token not resolving,Open,Medium
1004,Dan Wong,Slow query on PO screen,Open,High

Summary printed to the terminal:
Rows read:          7
Duplicates removed: 2
Blank rows removed: 1
Rows written:       4
Output:             tickets_cleaned.csv