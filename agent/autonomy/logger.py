import os
from datetime import datetime


class ZetaLogger:

    def __init__(self):

        self.file = os.path.expanduser(
            "~/cyprus/workspace/logs/zeta_activity.log"
        )


    def write(self, message):

        with open(self.file, "a") as f:

            f.write(
                f"{datetime.now()} - {message}\n"
            )

        print("[ZETA LOG]", message)


    # Compatibility method for ZETA modules
    def log(self, message):

        self.write(message)
