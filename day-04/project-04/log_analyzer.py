"""
Log Analyzer Script
Reads a log file, counts INFO, WARNING, and ERROR messages,
prints a summary, and writes the summary to log_summary.txt.
"""

import os

LOG_LEVELS = ["INFO", "WARNING", "ERROR"]


def analyze_log(file_path):
    """
    Analyze the log file and count log levels.
    """
    counts = {level: 0 for level in LOG_LEVELS}

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()

            if not lines:
                raise ValueError("Log file is empty.")

            for line in lines:
                for level in LOG_LEVELS:
                    if level in line:
                        counts[level] += 1

        return counts

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except ValueError as error:
        print(f"Error: {error}")
        return None


def write_summary(output_path, summary):
    """
    Write the summary to the output file.
    """
    with open(output_path, "w") as file:
        file.write("Log Summary\n")
        file.write("-----------\n")
        for level, count in summary.items():
            file.write(f"{level}: {count}\n")


def print_summary(summary):
    """
    Print the summary to the terminal.
    """
    print("\nLog Summary")
    print("-----------")
    for level, count in summary.items():
        print(f"{level}: {count}")


def main():
    # Get the directory where this script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Input and output files
    log_file = os.path.join(base_dir, "app.log")
    output_file = os.path.join(base_dir, "log_summary.txt")

    summary = analyze_log(log_file)

    if summary:
        print_summary(summary)
        write_summary(output_file, summary)
        print(f"\nSummary written to '{output_file}'")


if __name__ == "__main__":
    main()
