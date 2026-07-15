import os
import json
import shutil
from datetime import datetime


UPGRADE_LOG = "data/upgrade_history.json"
BACKUP_FOLDER = "data/backups"


class UpgradeManager:

    def __init__(self):
        os.makedirs(BACKUP_FOLDER, exist_ok=True)

        if not os.path.exists(UPGRADE_LOG):
            with open(UPGRADE_LOG, "w") as f:
                json.dump([], f, indent=2)


    def inspect(self):

        files = []

        for root, dirs, filenames in os.walk("agent"):
            for file in filenames:
                if file.endswith(".py"):
                    files.append(
                        os.path.join(root, file)
                    )

        return files


    def create_backup(self, filepath):

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        filename = filepath.replace(
            "/",
            "_"
        )

        backup = os.path.join(
            BACKUP_FOLDER,
            f"{timestamp}_{filename}"
        )

        shutil.copy(
            filepath,
            backup
        )

        return backup


    def propose(self, idea):

        entry = {
            "time": str(datetime.now()),
            "idea": idea,
            "status": "pending"
        }


        with open(UPGRADE_LOG,"r") as f:
            log=json.load(f)


        log.append(entry)


        with open(UPGRADE_LOG,"w") as f:
            json.dump(
                log,
                f,
                indent=2
            )


        return entry


    def status(self):

        with open(UPGRADE_LOG,"r") as f:
            return json.load(f)
