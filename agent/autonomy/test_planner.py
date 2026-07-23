from datetime import datetime


class TestPlanner:


    def __init__(self):

        self.name = "ZETA Test Planner"



    def create_tests(self, build_plan):

        print(
            "[ZETA TEST PLANNER] Creating validation plan"
        )


        task = build_plan.get(
            "task",
            "unknown task"
        )


        tests = {


            "planner": self.name,


            "task": task,


            "tests": [

                "unit test required",

                "integration test required",

                "regression test required"

            ],


            "validation_rules": [

                "existing features must continue working",

                "memory must save correctly",

                "memory must recall correctly"

            ],


            "rollback":

                "restore previous git tag if failed",


            "approval_required":

                True,


            "created":

                str(datetime.now())

        }


        print(
            "[ZETA TEST PLANNER] Validation plan ready"
        )


        return tests
