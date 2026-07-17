from agent.autonomy.task_manager import TaskManager
from agent.autonomy.developer_agent import DeveloperAgent
from agent.autonomy.experience_engine import ExperienceEngine


class ZetaWorker:

    def __init__(self):

        self.tasks = TaskManager()
        self.developer = DeveloperAgent()
        self.experience = ExperienceEngine()


    def run_once(self):

        print("[ZETA WORKER] Checking tasks")


        task_list = self.tasks.tasks


        active = [
            t for t in task_list
            if t["status"] == "active"
        ]


        if not active:

            print("[ZETA WORKER] No active tasks")
            return {
                "status": "idle"
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


        task["status"] = "complete"


        self.experience.record_cycle(
            {
                "module": "worker",
                "task": task["task"],
                "result": "completed"
            }
        )


        print(
            "[ZETA WORKER] Task complete"
        )


        return result
