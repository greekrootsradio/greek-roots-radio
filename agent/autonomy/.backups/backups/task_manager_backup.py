import os
import json
from datetime import datetime


class TaskManager:

    def __init__(self):

        self.file = os.path.expanduser(
            "~/cyprus/data/tasks.json"
        )

        self.tasks = self.load()


    def load(self):

        if os.path.exists(self.file):

            with open(self.file, "r") as f:
                return json.load(f)

        return {
            "active": [],
            "completed": [],
            "history": []
        }


    def save(self):

        with open(self.file, "w") as f:
            json.dump(
                self.tasks,
                f,
                indent=4
            )


    def create_task(self, goal, priority=50):

        task = {
            "task": goal,
            "priority": priority,
            "status": "active",
            "created": str(datetime.now())
        }

        self.tasks["active"].append(task)

        self.save()

        print(
            "[ZETA TASK] Created:",
            task["task"]
        )

        return task


    def get_next_task(self):

        if not self.tasks["active"]:
            return None

        self.tasks["active"].sort(
            key=lambda x: x["priority"],
            reverse=True
        )

        return self.tasks["active"][0]


    def complete_task(self, task):

        task["status"] = "completed"
        task["completed"] = str(datetime.now())

        self.tasks["active"].remove(task)

        self.tasks["completed"].append(task)

        self.tasks["history"].append(task)

        self.save()

        print(
            "[ZETA TASK] Completed:",
            task["task"]
        )


    def summary(self):

        return {
            "active": len(self.tasks["active"]),
            "completed": len(self.tasks["completed"]),
            "history": len(self.tasks["history"]),
            "time": str(datetime.now())
        }
