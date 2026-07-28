import os
import shutil
from datetime import datetime


class SelfImprovementManager:

    def __init__(self):
        self.root = os.path.expanduser("~/cyprus")
        self.backup_dir = os.path.join(
            self.root,
            "workspace/backups"
        )

        os.makedirs(
            self.backup_dir,
            exist_ok=True
        )


    def backup_file(self, filepath):

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        source = os.path.join(
            self.root,
            filepath
        )

        if not os.path.exists(source):
            return None

        backup = os.path.join(
            self.backup_dir,
            f"{timestamp}_{os.path.basename(filepath)}"
        )

        shutil.copy2(
            source,
            backup
        )

        return backup


    def approve_change(self, filepath):

        backup = self.backup_file(filepath)

        if backup:
            return {
                "status": "approved",
                "backup": backup
            }

        return {
            "status": "failed"
        }
