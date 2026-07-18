import datetime
import os
import sys

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


    def write(self,message):

        with open(self.log,"a") as f:
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


        SupervisorExecutor().execute(
            decision
        )


        self.write(
            "=== SUPERVISOR CYCLE COMPLETE ==="
        )



if __name__ == "__main__":

    ZetaSupervisorController().run_once()
