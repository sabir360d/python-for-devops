"""
Day 05 - Object-Oriented Log Analyzer
Refactored from Day 04 script to use classes.
"""

import os


class LogAnalyzer:
    LOG_LEVELS = ["INFO", "WARNING", "ERROR"]

    def __init__(self, log_file):
        """
        Initialize the log analyzer with the log file path.
        """
        self.log_file = log_file
        self.counts = {level: 0 for level in self.LOG_LEVELS}

    def read_logs(self):
        """
        Read log lines from the log file.
        """
        try:
            with open(self.log_file, "r") as file:
                lines = file.readlines()
                if not lines:
                    print("Log file is empty.")
                    return []
                return lines
        except FileNotFoundError:
            print(f"Log file not found: {self.log_file}")
            return []

    def analyze_logs(self, lines):
        """
        Count INFO, WARNING, and ERROR occurrences in the logs.
        """
        for line in lines:
            for level in self.LOG_LEVELS:
                if level in line:
                    self.counts[level] += 1
        return self.counts

    def print_summary(self):
        """
        Print log summary to terminal.
        """
        print("\nLog Summary")
        print("-----------")
        for level, count in self.counts.items():
            print(f"{level}: {count}")

    def write_summary(self, output_file="log_summary.txt"):
        """
        Write log summary to a file.
        """
        with open(output_file, "w") as file:
            file.write("Log Summary\n")
            file.write("-----------\n")
            for level, count in self.counts.items():
                file.write(f"{level}: {count}\n")
        print(f"\nSummary written to '{output_file}'")


def main():
    # Resolve file paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(base_dir, "app.log")
    output_file = os.path.join(base_dir, "log_summary.txt")

    # Instantiate LogAnalyzer and run
    analyzer = LogAnalyzer(log_file)
    lines = analyzer.read_logs()

    if not lines:
        print("No logs to analyze.")
        return

    analyzer.analyze_logs(lines)
    analyzer.print_summary()
    analyzer.write_summary(output_file)


if __name__ == "__main__":
    main()
