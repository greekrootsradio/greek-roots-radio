import os
import sys
import datetime

BASE_DIR = os.path.expanduser("~/cyprus")

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from agent.executive.planner import ExecutivePlanner


class ExecutiveBrain:

    def __init__(self):

        self.log = os.path.expanduser(
            "~/cyprus/workspace/logs/zeta_executive.log"
        )

        os.makedirs(
            os.path.dirname(self.log),
            exist_ok=True
        )

        self.planner = ExecutivePlanner()


    def write(self, message):

        with open(self.log, "a") as f:
            f.write(
                f"{datetime.datetime.now()} {message}\n"
            )


    def think(self):

        self.write(
            "=== EXECUTIVE THINK CYCLE ==="
        )

        goal = self.planner.next_goal()

        if goal is None:

            self.write(
                "No active goals"
            )

            return None


        self.write(
            f"Selected goal: {goal}"
        )

        return goal



if __name__ == "__main__":

    brain = ExecutiveBrain()

    result = brain.think()

    print(result)
