import json
import os
from datetime import datetime

from agent.memory.memory_manager import MemoryManager


class DecisionEngine:

    def __init__(self):

        self.goals_file = os.path.expanduser(
            "~/cyprus/data/goals.json"
        )

        self.memory = MemoryManager()


    def load_goals(self):

        with open(self.goals_file, "r") as f:
            return json.load(f)


    def choose_priority(self):

        memory = self.memory.summary()

        goals = self.load_goals()


        if isinstance(goals, dict):

            active = goals.get("active", [])

        else:

            active = goals


        if active:

            active = sorted(
                active,
                key=lambda x: x.get("priority", 0),
                reverse=True
            )

            top_goal = active[0]

        else:

            top_goal = None


        projects = memory.get(
            "projects",
            {}
        )


        user_goals = memory.get(
            "goals",
            []
        )


        tasks = memory.get(
            "tasks",
            []
        )


        pending_tasks = [
            t for t in tasks
            if t.get("status") != "completed"
        ]


        decision = {

            "goal": (
                top_goal["goal"]
                if top_goal
                else None
            ),

            "priority": (
                top_goal["priority"]
                if top_goal
                else 0
            ),

            "projects": list(
                projects.keys()
            ),

            "memory_goals": user_goals,

            "pending_tasks": len(
                pending_tasks
            ),

            "status": "active"

        }


        result = {

            "decision": decision,

            "time": str(
                datetime.now()
            )

        }


        print("[ZETA DECISION]")
        print(result)


        return result
