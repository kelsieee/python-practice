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
Output:             tickets_cleaned.csv`

# log_parser.py
A small Python script that reads a log file, counts how many lines contain each keyword, and prints a summary.

# What it does
1. Reads the log file one line at a time.
2. Checks each line for the keywords INFO, WARNING, ERROR and DEBUG.
3. Matches whole words only, so INFO is not counted inside INFORMATION.
4. Ignores upper/lower case, so error and ERROR count as the same keyword.
5. Counts a line once for every keyword it contains, so a line with two keywords adds to both counts.
6. Prints a summary of the counts for each keyword.

# Requirements
Python 3.6 or newer
No extra packages (standard library only)

 # Usage
python log_parser.py <log_file.log>

# Example

Input (sample.log):

2026-11-20 09:00:01 INFO  Service started
2026-11-20 09:00:02 DEBUG Loading config
2026-11-20 09:00:05 INFO  User login ok
2026-11-20 09:01:10 WARNING Slow query on PO screen (4.2s)

2026-11-20 09:02:33 ERROR Email token not resolved: #I_SUPP#
2026-11-20 09:02:34 ERROR Connection timeout while sending email
2026-11-20 09:03:00 INFO  More INFORMATION about the batch
2026-11-20 09:04:12 CRITICAL Database connection lost
2026-11-20 09:04:13 error retry failed after timeout
this line has no level at all

Command:

python log_parser.py sample.log

Summary printed to the terminal:

Summary of log file:
INFO: 3
WARNING: 1
ERROR: 3
DEBUG: 1