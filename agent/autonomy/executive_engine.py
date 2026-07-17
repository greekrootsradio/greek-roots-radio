from datetime import datetime

from agent.autonomy.decision_engine import DecisionEngine
from agent.autonomy.experience_engine import ExperienceEngine
from agent.autonomy.planner import PlannerAgent
from agent.autonomy.task_manager import TaskManager
from agent.autonomy.task_decomposer import TaskDecomposer


class ExecutiveEngine:

    def __init__(self):

        self.decision = DecisionEngine()
        self.experience = ExperienceEngine()
        self.planner = PlannerAgent()
        self.tasks = TaskManager()
        self.decomposer = TaskDecomposer()


    def think(self):

        print("[ZETA EXECUTIVE] Thinking cycle started")


        decision = self.decision.choose_priority()


        plan = self.planner.generate_plan()


        created_tasks = []


        if plan:

            breakdown = self.decomposer.decompose(
                plan["module"]
            )


            for item in breakdown["tasks"]:

                task = self.tasks.create_task(
                    item["task"],
                    item["priority"]
                )

                created_tasks.append(task)


        result = {

            "time": str(datetime.now()),

            "decision": decision,

            "plan": plan,

            "tasks": created_tasks,

            "status": "ready"

        }


        self.experience.record_cycle(
            {
                "module": "executive_engine",
                "result": "goal_decomposed"
            }
        )


        print("[ZETA EXECUTIVE] Goal decomposition complete")


        return result
