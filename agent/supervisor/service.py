import os
import sys
import time
import datetime


BASE_DIR = os.path.expanduser("~/cyprus")

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)


from agent.supervisor.controller import ZetaSupervisorController


class ZetaSupervisorService:


    def __init__(self):

        self.log = os.path.expanduser(
            "~/cyprus/workspace/logs/zeta_service.log"
        )

        os.makedirs(
            os.path.dirname(self.log),
            exist_ok=True
        )

        self.controller = ZetaSupervisorController()


    def write(self, message):

        with open(self.log, "a") as f:
            f.write(
                f"{datetime.datetime.now()} {message}\n"
            )


    def start(self):

        self.write(
            "===== ZETA SUPERVISOR SERVICE STARTED ====="
        )


        try:

            while True:

                self.write(
                    "Running supervisor cycle"
                )


                result = self.controller.run_once()


                self.write(
                    f"Supervisor result: {result}"
                )


                time.sleep(30)


        except KeyboardInterrupt:

            self.write(
                "===== ZETA SUPERVISOR SERVICE STOPPED ====="
            )


if __name__ == "__main__":

    service = ZetaSupervisorService()

    service.start()
