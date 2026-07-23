from datetime import datetime

from agent.autonomy.decision_engine import DecisionEngine
from agent.autonomy.experience_engine import ExperienceEngine
from agent.autonomy.planner import PlannerAgent
from agent.autonomy.task_manager import TaskManager
from agent.autonomy.executive_review import ExecutiveReview


class ExecutiveEngine:


    def __init__(self):

        self.decision = DecisionEngine()

        self.experience = ExperienceEngine()

        self.planner = PlannerAgent()

        self.tasks = TaskManager()

        self.review = ExecutiveReview()



    def think(self):

        print(
            "[ZETA EXECUTIVE] Thinking cycle started"
        )


        # -------------------------
        # MAKE DECISION
        # -------------------------

        decision = self.decision.choose_priority()



        # -------------------------
        # CREATE PLAN
        # -------------------------

        plan = self.planner.generate_plan(
            decision
        )



        # -------------------------
        # CREATE TASK
        # -------------------------

        task = self.tasks.create_task(
            plan["module"],
            plan.get(
                "priority",
                50
            )
        )



        # -------------------------
        # RECORD EXPERIENCE
        # -------------------------

        self.experience.record_cycle(

            {

                "decision": decision,

                "plan": plan,

                "task": task,

                "result": "created"

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



        # -------------------------
        # EXECUTIVE REFLECTION
        # -------------------------

        review = self.review.review_cycle(
            result
        )


        result["review"] = review



        print(
            "[ZETA EXECUTIVE] Decision complete"
        )


        return result



if __name__ == "__main__":


    engine = ExecutiveEngine()


    print(
        engine.think()
    )
