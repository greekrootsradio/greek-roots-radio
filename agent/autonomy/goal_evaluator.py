from datetime import datetime


class GoalEvaluator:


    def __init__(self):

        self.name = "goal_evaluator"



    def evaluate(self, action, result):

        print(
            "[ZETA EVALUATOR] Evaluating result"
        )


        evaluation = {

            "goal": action.get("goal"),

            "success": True,

            "result": result,

            "time": str(datetime.now())

        }


        print(
            "[ZETA EVALUATOR] Goal completed:",
            action.get("goal")
        )


        return evaluation
