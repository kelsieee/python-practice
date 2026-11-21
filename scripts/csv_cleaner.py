import csv
import sys

def clean_csv(input_file, output_file):
    read = blanks = duplicates = written = 0
    seen_rows = set() 

    #Rule of thumb: whenever you open a file for the csv module, to read or write, add newline="".
    with open(input_file, "r", newline='') as infile, \
    open(output_file, "w", newline='') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Read the header (and trim it too)
        header = next(reader, None) #The header is the first row of the CSV, and it holds column names, not data. empty file: returns None, no crash
        if header is None:
            print("Input file is empty.")
            return
        writer.writerow([cell.strip() for cell in header])

        for row in reader:
            read += 1
            # Trim whitespace from each cell
            row = [cell.strip() for cell in row] #[" 1001 ", " Alice Tan "] becomes ["1001", "Alice Tan"]

            # Skip blank rows
            if not any(row):
                blanks += 1
                continue     # done with this row, go to the next one

            # Skip duplicates
            row_tuple = tuple(row) #convert row to tuple so it can be added to a set - tuples are hashable, lists are not
            if row_tuple in seen_rows:
                duplicates += 1
                continue     # done with this row, go to the next one

            seen_rows.add(row_tuple)
            writer.writerow(row)
            written += 1

    print(f"Rows read: {read}")
    print(f"Blank rows removed: {blanks}")
    print(f"Duplicates removed: {duplicates}")
    print(f"Rows written: {written}")
    print(f"Cleaned CSV written to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python csv_cleaner.py <input_file.csv> ")
        #sys.exit(1) stops the script immediately. The 1 is an exit code: 0 means success and anything else means an error.
        sys.exit(1)

    input_file = sys.argv[1] #['csv_cleaner.py', 'tickets.csv'] -> tickets.csv
    output_file = (
        input_file.replace(".csv", "_cleaned.csv")
    )

    clean_csv(input_file, output_file)
