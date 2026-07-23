from datetime import datetime


class GoalEvaluator:


    def __init__(self):

        self.name = "goal_evaluator"



    def evaluate(self, action, result):

        print(
            "[ZETA EVALUATOR] Evaluating result"
        )


        success = False

        confidence = 0.0

        reason = "unknown"



        if isinstance(result, dict):

            status = result.get(
                "status",
                "unknown"
            )


            if status in [
                "completed",
                "success",
                "done"
            ]:

                success = True

                confidence = 1.0

                reason = "goal completed successfully"



            elif status in [
                "idle",
                "waiting"
            ]:

                success = False

                confidence = 0.5

                reason = "no work performed"



            elif status in [
                "failed",
                "error"
            ]:

                success = False

                confidence = 1.0

                reason = "goal execution failed"



            else:

                confidence = 0.2

                reason = "unknown execution state"



        evaluation = {

            "goal": action.get(
                "goal",
                "unknown"
            ),

            "success": success,

            "confidence": confidence,

            "reason": reason,

            "result": result,

            "time": str(
                datetime.now()
            )

        }



        if success:

            print(
                "[ZETA EVALUATOR] Goal succeeded:",
                evaluation["goal"]
            )


        else:

            print(
                "[ZETA EVALUATOR] Goal not completed:",
                evaluation["goal"]
            )


        print(
            "[ZETA EVALUATOR] Confidence:",
            confidence
        )


        return evaluation



if __name__ == "__main__":


    evaluator = GoalEvaluator()


    tests = [

        (
            {
                "goal": "test_success"
            },

            {
                "status": "completed"
            }

        ),

        (
            {
                "goal": "test_idle"
            },

            {
                "status": "idle"
            }

        )

    ]


    for action, result in tests:

        print(
            evaluator.evaluate(
                action,
                result
            )
        )
