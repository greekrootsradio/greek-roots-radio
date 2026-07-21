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

        print(
            "[ZETA EXECUTIVE] Thinking cycle started"
        )


        # -------------------------------
        # 1. MAKE DECISION
        # -------------------------------

        decision_result = self.decision.choose_priority()


        # DecisionEngine returns:
        #
        # {
        #   "decision": {
        #       "chosen_goal": "...",
        #       "score": ...
        #   }
        # }


        decision = decision_result.get(
            "decision",
            {}
        )



        # -------------------------------
        # 2. CREATE PLAN
        # -------------------------------

        plan = self.planner.generate_plan(
            decision
        )



        # -------------------------------
        # 3. CREATE TASK
        # -------------------------------

        task = self.tasks.create_task(
            plan.get(
                "module"
            ),
            plan.get(
                "priority",
                0
            )
        )



        # -------------------------------
        # 4. RECORD EXPERIENCE
        # -------------------------------

        self.experience.record(
            {
                "decision": decision,

                "plan": plan,

                "task": task
            }
        )



        result = {

            "time": str(
                datetime.now()
            ),

            "decision": decision,

            "plan": plan,

            "task": task,

            "status": "ready"

        }


        print(
            "[ZETA EXECUTIVE] Decision complete"
        )


        return result




if __name__ == "__main__":


    engine = ExecutiveEngine()


    print(
        engine.think()
    )
