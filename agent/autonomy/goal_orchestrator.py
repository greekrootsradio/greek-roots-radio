from agent.autonomy.goal_manager import GoalManager


class GoalOrchestrator:

    def __init__(self):
        self.goal_manager = GoalManager()

    def choose_goal(self):
        goal = self.goal_manager.get_next_goal()

        if goal:
            print("[ZETA ORCHESTRATOR] Selected goal:", goal)
        else:
            print("[ZETA ORCHESTRATOR] No goals available")

        return goal

    def create_action(self, goal):
        if not goal:
            return None

        action = {
            "goal": goal["goal"],
            "priority": goal["priority"],
            "instruction": "Execute goal: " + goal["goal"],
        }

        print("[ZETA ORCHESTRATOR] Action created:", action)
        return action
