import json
import os
from datetime import datetime


class GoalManager:

    def __init__(self):

        self.file = os.path.expanduser(
            "~/cyprus/data/goals.json"
        )

        self.load()


    def load(self):

        if os.path.exists(self.file):

            with open(self.file, "r") as f:
                self.goals = json.load(f)

        else:

            self.goals = {
                "active": [],
                "completed": [],
                "history": []
            }


    def save(self):

        with open(self.file, "w") as f:
            json.dump(
                self.goals,
                f,
                indent=4
            )


    def add_goal(self, name, priority=50):

        goal = {

            "name": name,
            "priority": priority,
            "created": str(datetime.now()),
            "status": "active"

        }


        self.goals["active"].append(goal)

        self.goals["history"].append(goal)

        self.save()

        print("[ZETA GOAL] Added")

        return goal



    def get_next_goal(self):

        if not self.goals["active"]:
            return None


        goal = sorted(
            self.goals["active"],
            key=lambda x:x["priority"],
            reverse=True
        )[0]


        return goal
