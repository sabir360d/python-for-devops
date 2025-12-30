"""
CLI Tool for DevOps
Use Day 05 OOP Log Analyzer using argparse
"""

import argparse
import os


class LogAnalyzer:
    LOG_LEVELS = ["INFO", "WARNING", "ERROR"]

    def __init__(self, log_file):
        self.log_file = log_file
        self.counts = {level: 0 for level in self.LOG_LEVELS}

    def read_logs(self):
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

    def analyze_logs(self, lines, level_filter=None):
        for line in lines:
            for level in self.LOG_LEVELS:
                if level in line:
                    if level_filter and level != level_filter:
                        continue
                    self.counts[level] += 1

    def print_summary(self):
        print("\nLog Summary")
        print("-----------")
        for level, count in self.counts.items():
            print(f"{level}: {count}")

    def write_summary(self, output_file):
        with open(output_file, "w") as file:
            file.write("Log Summary\n")
            file.write("-----------\n")
            for level, count in self.counts.items():
                file.write(f"{level}: {count}\n")
        print(f"\nSummary written to '{output_file}'")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="CLI Log Analyzer for DevOps Engineers"
    )

    parser.add_argument(
        "--file",
        required=True,
        help="Path to the log file"
    )

    parser.add_argument(
        "--out",
        default="log_summary.txt",
        help="Output file path (default: log_summary.txt)"
    )

    parser.add_argument(
        "--level",
        choices=["INFO", "WARNING", "ERROR"],
        help="Filter logs by level (optional)"
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    if not os.path.exists(args.file):
        print("Error: Log file does not exist.")
        return

    analyzer = LogAnalyzer(args.file)
    lines = analyzer.read_logs()

    if not lines:
        print("No logs to analyze.")
        return

    analyzer.analyze_logs(lines, args.level)
    analyzer.print_summary()
    analyzer.write_summary(args.out)


if __name__ == "__main__":
    main()
