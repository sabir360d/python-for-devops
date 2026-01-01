from fastapi import FastAPI, Query
import os
from typing import Optional

app = FastAPI(title="DevOps Log Analyzer API")


@app.get("/")
def root():
    """
    Root endpoint to describe the API
    """
    return {
        "message": "DevOps Log Analyzer API",
        "endpoints": ["/health", "/logs", "/docs"]
    }


class LogAnalyzer:
    """
    LogAnalyzer reads a log file and counts log levels.
    """

    LOG_LEVELS = ["INFO", "WARNING", "ERROR"]

    def __init__(self, log_file: str):
        self.log_file = log_file

    def read_logs(self) -> list[str]:
        """
        Read log file and return all lines.
        """
        if not os.path.exists(self.log_file):
            return []

        with open(self.log_file, "r") as file:
            return file.readlines()

    def analyze_logs(self, lines: list[str], level_filter: Optional[str] = None) -> dict:
        """
        Analyze logs and return count of each log level.
        Optional filtering by log level.
        """
        counts = {level: 0 for level in self.LOG_LEVELS}

        for line in lines:
            for level in self.LOG_LEVELS:
                if level in line:
                    if level_filter and level != level_filter:
                        continue
                    counts[level] += 1

        return counts


# -------------------- API Endpoints --------------------

@app.get("/health")
def health_check():
    """
    Health check endpoint
    """
    return {
        "status": "ok",
        "service": "log-analyzer",
        "message": "API is healthy"
    }


@app.get("/logs")
def analyze_logs(
    level: Optional[str] = Query(
        default=None,
        description="Filter by log level: INFO, WARNING, ERROR"
    )
):
    """
    Analyze application logs and return log level summary.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(base_dir, "app.log")

    analyzer = LogAnalyzer(log_file)
    lines = analyzer.read_logs()

    if not lines:
        return {
            "error": "Log file not found or empty"
        }

    summary = analyzer.analyze_logs(lines, level)

    return {
        "log_file": log_file,
        "filter": level,
        "summary": summary
    }
