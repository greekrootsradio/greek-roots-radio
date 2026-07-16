import os
import json
from datetime import datetime


class GoalManager:

    def __init__(self):

        self.file = os.path.expanduser(
            "~/cyprus/data/goals.json"
        )

        self.goals = {}

        self.load()


    def load(self):

        if os.path.exists(self.file):

            with open(self.file, "r") as f:
                self.goals = json.load(f)


            # Upgrade old ZETA goal format
            if isinstance(self.goals, list):

                print(
                    "[ZETA GOAL] Migrating old goal format"
                )

                self.goals = {

                    "active": self.goals,

                    "completed": [],

                    "history": self.goals.copy()

                }

                self.save()


        else:

            self.goals = {

                "active": [],

                "completed": [],

                "history": []

            }

            self.save()



    def save(self):

        os.makedirs(
            os.path.dirname(self.file),
            exist_ok=True
        )

        with open(self.file, "w") as f:

            json.dump(
                self.goals,
                f,
                indent=4
            )



    def add_goal(self, name, priority):

        goal = {

            "goal": name,

            "priority": priority,

            "status": "active",

            "created": str(datetime.now())

        }


        self.goals["active"].append(goal)

        self.goals["history"].append(goal)

        self.save()


        print(
            "[ZETA GOAL] Added:",
            name
        )


        return goal



    def get_next_goal(self):

        if not self.goals["active"]:

            return None


        sorted_goals = sorted(

            self.goals["active"],

            key=lambda x: x["priority"],

            reverse=True

        )


        return sorted_goals[0]



    def complete_goal(self, goal_name):

        for goal in self.goals["active"]:

            if goal["goal"] == goal_name:

                goal["status"] = "completed"

                self.goals["completed"].append(goal)

                self.goals["active"].remove(goal)

                self.save()


                print(
                    "[ZETA GOAL] Completed:",
                    goal_name
                )


                return goal


        return None



    def summary(self):

        return {

            "active":

            len(self.goals["active"]),


            "completed":

            len(self.goals["completed"]),


            "history":

            len(self.goals["history"]),


            "time":

            str(datetime.now())

        }
