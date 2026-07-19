import json
import os


class GoalManager:

    def __init__(self):

        self.file = os.path.expanduser(
            "~/cyprus/workspace/goals.json"
        )

        os.makedirs(
            os.path.dirname(self.file),
            exist_ok=True
        )

        if not os.path.exists(self.file):
            self.save([])

    def load(self):

        with open(self.file, "r") as f:
            return json.load(f)

    def save(self, goals):

        with open(self.file, "w") as f:
            json.dump(goals, f, indent=4)

    def add_goal(self, name, priority=5):

        goals = self.load()

        goals.append({
            "name": name,
            "priority": priority,
            "status": "active"
        })

        self.save(goals)

    def active_goals(self):

        goals = self.load()

        return [
            g for g in goals
            if g["status"] == "active"
        ]


if __name__ == "__main__":

    manager = GoalManager()

    manager.add_goal(
        "Keep Greek Roots Radio online",
        1
    )

    print(
        manager.active_goals()
    )
