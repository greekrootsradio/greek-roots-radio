from datetime import datetime

from agent.autonomy.executive_engine import ExecutiveEngine
from agent.autonomy.goal_manager import GoalManager
from agent.autonomy.self_improvement import SelfImprovementEngine


class AutonomousBrain:

    def __init__(self):

        self.executive = ExecutiveEngine()
        self.goals = GoalManager()
        self.improvement = SelfImprovementEngine()


    def run(self):

        print("[ZETA BRAIN] Autonomous cycle starting")

        decision = self.executive.think()

        goal = self.goals.get_next_goal()

        analysis = self.improvement.analyse()


        result = {
            "time": str(datetime.now()),
            "decision": decision,
            "current_goal": goal,
            "improvement": analysis,
            "status": "cycle_complete"
        }


        print("[ZETA BRAIN] Cycle complete")

        return result
