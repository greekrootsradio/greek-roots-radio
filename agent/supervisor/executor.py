import datetime
import os

from agent.supervisor.actions import SupervisorActions


class SupervisorExecutor:


    def __init__(self):

        self.log = os.path.expanduser(
            "~/cyprus/workspace/logs/zeta_executor.log"
        )

        self.actions = SupervisorActions()


    def write(self, message):

        with open(self.log, "a") as f:
            f.write(
                f"{datetime.datetime.now()} {message}\n"
            )


    def execute(self, decision):

        self.write(
            f"Executing decision: {decision}"
        )


        if decision == "restart_core":

            self.write(
                "CORE restart action started"
            )

            return self.actions.restart_core()



        if decision == "restart_ollama":

            self.write(
                "OLLAMA restart action started"
            )

            return self.actions.restart_ollama()



        if decision == "repair_memory":

            self.write(
                "MEMORY repair action started"
            )

            return self.actions.repair_memory()



        self.write(
            "No action required"
        )

        return "healthy"



if __name__ == "__main__":

    executor = SupervisorExecutor()

    print(
        executor.execute("healthy")
    )
