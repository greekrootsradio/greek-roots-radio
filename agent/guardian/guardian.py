import os
import subprocess
from datetime import datetime


class ZetaGuardian:

    def __init__(self):
        self.base = os.path.expanduser("~/cyprus")
        self.log_file = os.path.join(
            self.base,
            "workspace/logs/zeta_guardian.log"
        )

    def log(self, message):
        os.makedirs(
            os.path.dirname(self.log_file),
            exist_ok=True
        )

        with open(self.log_file, "a") as f:
            f.write(
                f"{datetime.now()} | {message}\n"
            )

    def check_git(self):

        try:
            result = subprocess.check_output(
                ["git", "status", "--porcelain"],
                cwd=self.base
            ).decode()

            if result.strip():
                return {
                    "status": "changes_detected",
                    "details": result.splitlines()
                }

            return {
                "status": "clean"
            }

        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }


    def check_backups(self):

        backup_path = os.path.join(
            self.base,
            "workspace/backups"
        )

        if os.path.exists(backup_path):
            backups = os.listdir(backup_path)

            return {
                "status": "available",
                "count": len(backups)
            }

        return {
            "status": "missing"
        }


    def health_report(self):

        report = {
            "time": str(datetime.now()),
            "git": self.check_git(),
            "backups": self.check_backups()
        }

        self.log(
            str(report)
        )

        return report
