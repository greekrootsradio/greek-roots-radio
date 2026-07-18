import datetime
import os
import sys
import time

BASE_DIR = os.path.expanduser("~/cyprus")

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from agent.supervisor.health import ZetaHealth
from agent.supervisor.decision import SupervisorDecision
from agent.supervisor.executor import SupervisorExecutor


class ZetaSupervisorController:

    def __init__(self):

        self.log = os.path.expanduser(
            "~/cyprus/workspace/logs/zeta_controller.log"
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

    def run_once(self):

        self.write(
            "=== SUPERVISOR CYCLE START ==="
        )

        health = ZetaHealth().check()

        self.write(
            f"Health result: {health}"
        )

        decision = SupervisorDecision().evaluate(
            health
        )

        self.write(
            f"Decision: {decision}"
        )

        result = SupervisorExecutor().execute(
            decision
        )

        self.write(
            f"Action result: {result}"
        )

        self.write(
            "=== SUPERVISOR CYCLE COMPLETE ==="
        )

        return result

    def run_forever(self, interval=30):

        self.write(
            "===== ZETA SUPERVISOR STARTED ====="
        )

        while True:

            try:

                self.run_once()

            except Exception as e:

                self.write(
                    f"Supervisor Error: {e}"
                )

            time.sleep(interval)


if __name__ == "__main__":

    controller = ZetaSupervisorController()

    controller.run_forever()
