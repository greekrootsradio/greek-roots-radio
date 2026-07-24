from datetime import datetime


class Executor:

    def __init__(self):
        self.name = "ZETA Executor"

    def execute(self, plan):

        print("[ZETA EXECUTOR] Starting execution")

        completed = []

        for step in plan["steps"]:

            print(f"[ZETA EXECUTOR] {step}")

            completed.append(
                {
                    "step": step,
                    "status": "completed",
                    "time": str(datetime.now())
                }
            )

        print("[ZETA EXECUTOR] Execution complete")

        return {
            "status": "completed",
            "completed_steps": completed,
            "finished": str(datetime.now())
        }
