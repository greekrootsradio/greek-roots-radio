import os
import sys
import time
import datetime

BASE_DIR = os.path.expanduser("~/cyprus")

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from agent.executive.brain import ExecutiveBrain


class ExecutiveScheduler:

    def __init__(self):

        self.log = os.path.expanduser(
            "~/cyprus/workspace/logs/zeta_scheduler.log"
        )

        os.makedirs(
            os.path.dirname(self.log),
            exist_ok=True
        )

        self.brain = ExecutiveBrain()


    def write(self, message):

        with open(self.log, "a") as f:
            f.write(
                f"{datetime.datetime.now()} {message}\n"
            )


    def run_once(self):

        self.write(
            "Scheduler cycle started"
        )

        goal = self.brain.think()

        if goal:

            self.write(
                f"Scheduled goal: {goal}"
            )

        else:

            self.write(
                "No work scheduled"
            )

        return goal


if __name__ == "__main__":

    scheduler = ExecutiveScheduler()

    print(
        scheduler.run_once()
    )
