import time
import datetime
import os
import sys


BASE_DIR = os.path.expanduser("~/cyprus")

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)


from agent.supervisor.controller import ZetaSupervisorController


class ZetaWatchdog:


    def __init__(self):

        self.log = os.path.expanduser(
            "~/cyprus/workspace/logs/zeta_watchdog.log"
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


    def run(self):

        self.write(
            "=== ZETA WATCHDOG SUPERVISOR MODE STARTED ==="
        )

        controller = ZetaSupervisorController()


        while True:

            self.write(
                "Starting supervisor cycle"
            )


            try:

                controller.run_once()


                self.write(
                    "Supervisor cycle completed"
                )


            except Exception as e:

                self.write(
                    f"Supervisor cycle error: {e}"
                )


            time.sleep(300)



if __name__ == "__main__":

    ZetaWatchdog().run()
