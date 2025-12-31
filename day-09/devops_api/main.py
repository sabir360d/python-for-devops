from fastapi import FastAPI, Query
import os

app = FastAPI(title="DevOps Log Analyzer API")

@app.get("/")
def root():
    return {
        "message": "DevOps Log Analyzer API",
        "endpoints": ["/health", "/logs", "/docs"]
    }

class LogAnalyzer:
    LOG_LEVELS = ["INFO", "WARNING", "ERROR"]

    def __init__(self, log_file):
        self.log_file = log_file
        self.counts = {level: 0 for level in self.LOG_LEVELS}

    def read_logs(self):
        if not os.path.exists(self.log_file):
            return []

        with open(self.log_file, "r") as file:
            lines = file.readlines()
            return lines

    def analyze_logs(self, lines, level_filter=None):
        for line in lines:
            for level in self.LOG_LEVELS:
                if level in line:
                    if level_filter and level != level_filter:
                        continue
                    self.counts[level] += 1
        return self.counts


# API Endpoints

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "log-analyzer",
        "message": "API is healthy"
    }


@app.get("/logs")
def analyze_logs(
    level: str | None = Query(default=None, description="Filter by log level")
):
    """
    Analyze logs and return counts.
    Optional query param: ?level=INFO|WARNING|ERROR
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
