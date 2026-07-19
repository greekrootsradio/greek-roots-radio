import os
import sys
import time
import datetime


BASE_DIR = os.path.expanduser("~/cyprus")

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)


from agent.supervisor.controller import ZetaSupervisorController
from agent.executive.brain import ExecutiveBrain
from agent.executive.action import ExecutiveAction


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

        self.executive = ExecutiveBrain()

        self.action = ExecutiveAction()



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


                health = self.controller.run_once()


                self.write(
                    f"Supervisor result: {health}"
                )


                goal = self.executive.think()


                self.write(
                    f"Executive goal: {goal}"
                )


                result = self.action.execute(
                    goal
                )


                self.write(
                    f"Executive action result: {result}"
                )


            except Exception as e:

                self.write(
                    f"SERVICE ERROR: {e}"
                )


            time.sleep(30)



if __name__ == "__main__":

    service = ZetaSupervisorService()

    service.start()
