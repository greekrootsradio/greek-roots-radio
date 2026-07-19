import os
import sys

BASE_DIR = os.path.expanduser("~/cyprus")

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from agent.executive.goals import GoalManager


class ExecutivePlanner:

    def __init__(self):
        self.goals = GoalManager()

    def next_goal(self):

        goals = self.goals.active_goals()

        if not goals:
            return None

        goals.sort(
            key=lambda g: g["priority"]
        )

        return goals[0]


if __name__ == "__main__":

    planner = ExecutivePlanner()

    print(planner.next_goal())
