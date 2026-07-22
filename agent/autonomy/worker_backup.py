import os
from datetime import datetime

from agent.autonomy.task_manager import TaskManager
from agent.autonomy.developer_agent import DeveloperAgent


class ZetaWorker:

    def __init__(self):

        self.tasks = TaskManager()
        self.developer = DeveloperAgent()


    def run_once(self):

        print("[ZETA WORKER] Checking tasks")


        active = self.tasks.tasks["active"]


        if not active:

            print("[ZETA WORKER] No active tasks")

            return {
                "status": "idle",
                "time": str(datetime.now())
            }


        # highest priority task first

        active.sort(
            key=lambda x: x["priority"],
            reverse=True
        )


        task = active[0]


        print(
            "[ZETA WORKER] Selected:",
            task["task"]
        )


        result = self.developer.build(
            task["task"]
        )


        if result["status"] == "complete":

            self.tasks.complete_task(
                task
            )


            print(
                "[ZETA WORKER] Task completed"
            )


        return {

            "task": task,

            "result": result,

            "status": "complete",

            "time": str(datetime.now())

        }
