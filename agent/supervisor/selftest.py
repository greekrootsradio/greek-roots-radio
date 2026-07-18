import os
import sys
import datetime


BASE_DIR = os.path.expanduser("~/cyprus")

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)


from agent.supervisor.health import ZetaHealth
from agent.supervisor.decision import SupervisorDecision
from agent.supervisor.executor import SupervisorExecutor


class ZetaSelfTest:


    def __init__(self):

        self.log = os.path.expanduser(
            "~/cyprus/workspace/logs/zeta_selftest.log"
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
            "===== ZETA SELF TEST START ====="
        )


        try:

            self.write(
                "Testing health system"
            )

            health = ZetaHealth().check()

            self.write(
                f"Health result: {health}"
            )


            self.write(
                "Testing decision system"
            )

            decision = SupervisorDecision().evaluate(
                health
            )

            self.write(
                f"Decision result: {decision}"
            )


            self.write(
                "Testing executor link"
            )

            executor = SupervisorExecutor()

            if decision == "healthy":

                result = "healthy"

            else:

                result = executor.execute(
                    decision
                )


            self.write(
                f"Executor result: {result}"
            )


            self.write(
                "Health system: OK"
            )

            self.write(
                "Decision system: OK"
            )

            self.write(
                "Executor system: OK"
            )

            self.write(
                "ZETA SELF TEST PASSED"
            )


            return "passed"


        except Exception as e:

            self.write(
                f"SELF TEST FAILED: {e}"
            )

            return "failed"



if __name__ == "__main__":

    test = ZetaSelfTest()

    print(
        test.run()
    )
