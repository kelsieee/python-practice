import sys
import re

DEFAULT_KEYWORDS = ("INFO", "WARNING", "ERROR", "DEBUG")
# Defined once, importable, so that the same keywords can be used in other scripts, like log_analyzer.py
# Tuple is immutable, so it cannot be changed accidentally. Lists are mutable, so they can be changed accidentally.

def log_parser(log_file, keywords=DEFAULT_KEYWORDS):
    """
    Parses the given log file and counts lines by keyword. It also prints a summary of the counts for each keyword.
    Args:
        log_file (str): Path to the log file. 
        keywords (tuple): A tuple of keywords to search for in the log file.
    """
    counts = {kw: 0 for kw in keywords} #short for: counts = dict.fromkeys(keywords, 0) #creates a dictionary with keys from keywords and values set to 0
    """
    tricks used in the regex pattern:
    compile(rf"\b{re.escape(kw)}\b", re.IGNORECASE) creates a regex pattern that matches the keyword as a whole word, ignoring case.
    \b -> word boundary, so "INFO" matches "INFO" but not "INFORMATION"
    rf = raw string format, so that backslashes are treated as literal characters in the regex pattern
    escape(kw) -> escapes any special characters in the keyword, so that they are treated as literal characters in the regex pattern
    ignorecase -> makes the regex pattern case-insensitive, so that "INFO" matches "info", "Info", etc.
    The patterns dictionary maps each keyword to its corresponding compiled regex pattern, which is used to search for the keyword in each line of the log file.  
    shape: { key : value   for item in collection }
    {
    "INFO":    re.compile(r"\bINFO\b", re.IGNORECASE),
    "WARNING": re.compile(r"\bWARNING\b", re.IGNORECASE),
    "ERROR":   re.compile(r"\bERROR\b", re.IGNORECASE),
    "DEBUG":   re.compile(r"\bDEBUG\b", re.IGNORECASE),
    }
    """
    patterns = {
        kw: re.compile(rf"\b{re.escape(kw)}\b", re.IGNORECASE) 
        for kw in keywords
    }

    try:
        with open(log_file, "r", encoding="utf-8", errors="replace") as file:
            for line in file:
                for keyword, pattern in patterns.items():
                    if pattern.search(line): #matches the pattern in the line, returns a match object if found <re.Match object; span=(11, 16), match='ERROR'>, None if not found
                        counts[keyword] += 1
    except FileNotFoundError:
        print(f"Error: The file {log_file} does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
        sys.exit(1)

    print_summary(counts)


def print_summary(counts):
    """
    Prints a summary of the counts for each keyword.
    Args:
        counts (dict): A dictionary containing the counts for each keyword.
    """
    print("Summary of log file:")
    for keyword, count in counts.items():
        print(f"{keyword}: {count}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python log_parser.py <log_file.log>")
        sys.exit(1)

    log_file = sys.argv[1]
    log_parser(log_file)


if __name__ == "__main__":
    main()