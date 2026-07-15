import os
import shutil
from datetime import datetime


class PatchManager:

    def __init__(self):

        self.root = os.path.expanduser("~/cyprus")

        self.backup = os.path.join(
            self.root,
            "workspace/backups"
        )

        os.makedirs(self.backup, exist_ok=True)


    def backup_file(self, filepath):

        name = os.path.basename(filepath)

        destination = os.path.join(
            self.backup,
            name + "." + datetime.now().strftime("%Y%m%d%H%M%S")
        )

        shutil.copy(filepath, destination)

        print(
            f"[ZETA PATCH] Backup created: {destination}"
        )

        return destination


    def apply_patch(self, filepath, new_code):

        self.backup_file(filepath)

        with open(filepath,"w") as f:
            f.write(new_code)

        print(
            f"[ZETA PATCH] Updated {filepath}"
        )
