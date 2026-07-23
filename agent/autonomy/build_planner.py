from datetime import datetime


class BuildPlanner:


    def __init__(self):

        self.name = "ZETA Build Planner"



    def create_plan(self, proposal):

        print(
            "[ZETA BUILD PLANNER] Creating implementation plan"
        )


        task = proposal.get(
            "task",
            "unknown task"
        )


        plan = {

            "planner": self.name,

            "task": task,

            "files_to_create": [

                "agent/memory/storage.py"

            ],

            "files_to_modify": [

                "agent/brain.py"

            ],

            "tests_required": [

                "memory save test",

                "memory recall test"

            ],

            "rollback":

                "git checkpoint required",


            "approval_required":

                True,


            "created":

                str(datetime.now())

        }


        print(
            "[ZETA BUILD PLANNER] Plan ready"
        )


        return plan
