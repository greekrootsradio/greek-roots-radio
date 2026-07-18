import time
import datetime
import os

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


        while True:

            try:

                self.write(
                    "Running supervisor cycle"
                )

                self.controller.run_once()


            except Exception as e:

                self.write(
                    f"SERVICE ERROR: {e}"
                )


            time.sleep(30)



if __name__ == "__main__":

    service = ZetaSupervisorService()

    service.start()
