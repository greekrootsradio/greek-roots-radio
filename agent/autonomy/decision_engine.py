import json
import os
from datetime import datetime


class DecisionEngine:

    def __init__(self):

        self.goals_file = os.path.expanduser(
            "~/cyprus/data/goals.json"
        )

        self.history_file = os.path.expanduser(
            "~/cyprus/data/development_history.json"
        )


    def load_goals(self):

        if not os.path.exists(self.goals_file):
            return []

        with open(self.goals_file, "r") as f:
            return json.load(f)


    def choose_priority(self):

        goals = self.load_goals()

        if goals:

            priority = goals[0]

        else:

            priority = {
                "goal": "improve autonomy",
                "priority": 100
            }


        decision = {

            "decision": priority,
            "time": str(datetime.now())

        }


        print("[ZETA DECISION]")
        print(decision)

        return decision
