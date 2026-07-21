from datetime import datetime

from agent.autonomy.decision_engine import DecisionEngine
from agent.autonomy.experience_engine import ExperienceEngine
from agent.autonomy.planner import PlannerAgent
from agent.autonomy.task_manager import TaskManager


class ExecutiveEngine:

    def __init__(self):

        self.decision = DecisionEngine()
        self.experience = ExperienceEngine()
        self.planner = PlannerAgent()
        self.tasks = TaskManager()


    def think(self):

        print("[ZETA EXECUTIVE] Thinking cycle started")


        decision = self.decision.choose_priority()


        plan = self.planner.generate_plan()


        created_task = None

        if plan:

            created_task = self.tasks.create_task(
                plan["module"],
                plan["priority"]
            )


        result = {
            "time": str(datetime.now()),
            "decision": decision,
            "plan": plan,
            "task": created_task,
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
