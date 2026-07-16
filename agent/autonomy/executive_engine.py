from datetime import datetime

from agent.autonomy.decision_engine import DecisionEngine
from agent.autonomy.experience_engine import ExperienceEngine
from agent.autonomy.planner import PlannerAgent


class ExecutiveEngine:

    def __init__(self):

        self.decision = DecisionEngine()
        self.experience = ExperienceEngine()
        self.planner = PlannerAgent()


    def think(self):

        print("[ZETA EXECUTIVE] Thinking cycle started")


        decision = self.decision.choose_priority()

        plan = self.planner.generate_plan()


        result = {
            "time": str(datetime.now()),
            "decision": decision,
            "plan": plan,
            "status": "ready"
        }


        self.experience.record_cycle(
            {
                "module": "executive_engine",
                "result": "decision_complete"
            }
        )


        print("[ZETA EXECUTIVE] Decision complete")

        return result
