import json
from datetime import datetime


class TaskDecomposer:

    def __init__(self):

        self.patterns = {

            "Build permanent memory system": [
                {
                    "task": "Design memory architecture",
                    "priority": 100
                },
                {
                    "task": "Create memory storage module",
                    "priority": 90
                },
                {
                    "task": "Create memory retrieval system",
                    "priority": 80
                },
                {
                    "task": "Add memory indexing",
                    "priority": 70
                },
                {
                    "task": "Test permanent memory persistence",
                    "priority": 60
                }
            ]

        }


    def decompose(self, goal):

        print(
            "[ZETA DECOMPOSER] Analysing goal:",
            goal
        )


        if goal in self.patterns:

            tasks = self.patterns[goal]

        else:

            tasks = [
                {
                    "task": f"Research {goal}",
                    "priority": 50
                },
                {
                    "task": f"Design {goal}",
                    "priority": 40
                },
                {
                    "task": f"Build {goal}",
                    "priority": 30
                },
                {
                    "task": f"Test {goal}",
                    "priority": 20
                }
            ]


        result = {

            "goal": goal,

            "tasks": tasks,

            "created": str(datetime.now())

        }


        print(
            "[ZETA DECOMPOSER] Created",
            len(tasks),
            "tasks"
        )


        return result
