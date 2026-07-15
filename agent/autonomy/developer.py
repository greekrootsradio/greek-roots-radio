import os
from datetime import datetime


class DeveloperAgent:
    def __init__(self):
        self.project_root = os.path.expanduser("~/cyprus")
        self.workspace = os.path.join(self.project_root, "workspace")
        self.proposals = os.path.join(self.workspace, "proposals")

    def scan_project(self):
        project_files = []

        for root, dirs, files in os.walk(self.project_root):
            # Ignore Git metadata and workspace artifacts
            dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", "workspace")]

            for file in files:
                if file.endswith(".py"):
                    project_files.append(os.path.join(root, file))

        return sorted(project_files)

    def generate_report(self):
        files = self.scan_project()

        report = [
            "ZETA Developer Report",
            f"Generated: {datetime.now()}",
            "",
            f"Python files found: {len(files)}",
            ""
        ]

        for f in files:
            report.append(f)

        report_path = os.path.join(
            self.proposals,
            "developer_report.txt"
        )

        with open(report_path, "w") as fp:
            fp.write("\n".join(report))

        print(f"[Developer] Report written to {report_path}")
