import os
import shutil
from datetime import datetime


class SelfMonitor:

    def __init__(self):
        self.base = os.path.expanduser("~/cyprus")
        self.report = os.path.join(
            self.base,
            "workspace",
            "logs",
            "health_report.txt"
        )

    def check(self):

        status = {
            "time": str(datetime.now()),
            "memory": os.path.exists(
                os.path.join(self.base, "memory.json")
            ),
            "workspace": os.path.exists(
                os.path.join(self.base, "workspace")
            ),
        }

        total, used, free = shutil.disk_usage(self.base)

        status["disk_free_gb"] = round(
            free / (1024 ** 3),
            2
        )

        os.makedirs(
            os.path.dirname(self.report),
            exist_ok=True
        )

        with open(self.report, "w") as f:
            for key, value in status.items():
                f.write(f"{key}: {value}\n")

        print("[Monitor] Health report updated")

        return status
