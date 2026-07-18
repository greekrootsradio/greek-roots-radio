import datetime
import os


class SupervisorExecutor:

    def __init__(self):

        self.log = os.path.expanduser(
            "~/cyprus/workspace/logs/zeta_executor.log"
        )


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
                "CORE restart requested"
            )

            return "core_restart_requested"


        if decision == "restart_ollama":

            self.write(
                "OLLAMA restart requested"
            )

            return "ollama_restart_requested"


        if decision == "repair_memory":

            self.write(
                "MEMORY repair requested"
            )

            return "memory_repair_requested"


        self.write(
            "No action required"
        )

        return "healthy"
        

if __name__ == "__main__":

    executor = SupervisorExecutor()

    print(
        executor.execute("healthy")
    )
