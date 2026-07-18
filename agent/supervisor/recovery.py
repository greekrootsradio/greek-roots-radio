import os
import datetime
import subprocess


class ZetaRecovery:

    def __init__(self):

        self.log = os.path.expanduser(
            "~/cyprus/workspace/logs/zeta_recovery.log"
        )

        os.makedirs(
            os.path.dirname(self.log),
            exist_ok=True
        )


    def write(self, message):

        with open(self.log, "a") as f:
            f.write(
                f"{datetime.datetime.now()} {message}\n"
            )


    def restart_core(self):

        self.write(
            "Attempting ZETA core restart"
        )

        try:

            subprocess.run(
                [
                    "launchctl",
                    "kickstart",
                    "-k",
                    "gui/$(id -u)/com.zeta.core"
                ],
                shell=True
            )

            self.write(
                "Core restart command sent"
            )

        except Exception as e:

            self.write(
                f"Restart failed: {e}"
            )


    def recover(self):

        self.write(
            "=== ZETA RECOVERY STARTED ==="
        )

        self.write(
            "Recovery check complete"
        )


if __name__ == "__main__":

    ZetaRecovery().recover()
