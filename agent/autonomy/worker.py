from datetime import datetime

from agent.autonomy.task_manager import TaskManager
from agent.autonomy.developer_agent import DeveloperAgent


class ZetaWorker:


    def __init__(self):

        self.tasks = TaskManager()

        self.developer = DeveloperAgent()



    def run(self):

        return self.run_once()



    def run_once(self):

        print(
            "[ZETA WORKER] Checking tasks"
        )


        active = self.tasks.tasks["active"]


        if not active:

            print(
                "[ZETA WORKER] No active tasks"
            )


            return {

                "status": "idle",

                "time": str(
                    datetime.now()
                )

            }



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


        success_states = [

            "complete",
            "completed",
            "success",
            "passed"

        ]


        if result.get(
            "status"
        ) in success_states:


            self.tasks.complete_task(
                task
            )


            print(
                "[ZETA WORKER] Task completed"
            )


            worker_status = "completed"


        else:

            worker_status = "failed"



        return {

            "task": task,

            "result": result,

            "status": worker_status,

            "time": str(
                datetime.now()
            )

        }



if __name__ == "__main__":


    worker = ZetaWorker()


    print(
        worker.run()
    )
