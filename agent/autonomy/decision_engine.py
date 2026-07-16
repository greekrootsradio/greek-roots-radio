import json
import os
from datetime import datetime


class DecisionEngine:

    def __init__(self):

        self.goals_file = os.path.expanduser(
            "~/cyprus/data/goals.json"
        )


    def load_goals(self):

        with open(self.goals_file, "r") as f:
            return json.load(f)


    def choose_priority(self):

        goals = self.load_goals()

        # Support new Goal Manager format
        if isinstance(goals, dict):

            active = goals.get("active", [])

        else:

            active = goals


        if not active:

            return {
                "decision": None,
                "time": str(datetime.now())
            }


        # Sort highest priority first

        active = sorted(
            active,
            key=lambda x: x.get("priority",0),
            reverse=True
        )


        priority = active[0]


        result = {

            "decision": {
                "goal": priority["goal"],
                "priority": priority["priority"],
                "status": priority.get(
                    "status",
                    "active"
                )
            },

            "time": str(datetime.now())

        }


        print("[ZETA DECISION]")
        print(result)

        return result
