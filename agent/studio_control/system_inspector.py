import os
import platform
import shutil
import subprocess
from datetime import datetime


class StudioInspector:

    def report(self):

        disk = shutil.disk_usage("/")

        return {
            "time": str(datetime.now()),

            "system": {
                "computer": platform.node(),
                "os": platform.platform(),
                "python": platform.python_version()
            },

            "resources": {
                "disk_total_gb": round(disk.total / 1024**3,2),
                "disk_free_gb": round(disk.free / 1024**3,2)
            },

            "user": os.getenv("USER"),

            "processes": self.processes()
        }


    def processes(self):

        result = subprocess.check_output(
            ["ps","-ax"]
        ).decode()

        return result.splitlines()[:20]
