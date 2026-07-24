from datetime import datetime


class ImprovementPlanner:

    def __init__(self):

        self.name = "ZETA Improvement Planner"


    def create_plan(
        self,
        problem,
        objective
    ):

        return {

            "agent":
                self.name,

            "problem":
                problem,

            "objective":
                objective,

            "plan":
                [
                    "analyse current behaviour",
                    "identify possible improvement",
                    "prepare proposal",
                    "request approval",
                    "run validation"
                ],

            "status":
                "awaiting approval",

            "created":
                str(datetime.now())

        }
