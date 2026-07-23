from datetime import datetime


class ImplementationController:


    def __init__(self):

        self.name = "ZETA Implementation Controller"



    def prepare(self, proposal, build_plan, test_plan):

        print(
            "[ZETA IMPLEMENTATION] Preparing execution package"
        )


        package = {

            "controller": self.name,

            "task": proposal.get(
                "task",
                "unknown task"
            ),

            "proposal_status": proposal.get(
                "status",
                "unknown"
            ),

            "build_plan": build_plan,

            "test_plan": test_plan,

            "execution_allowed": False,

            "reason":

                "waiting for implementation approval",

            "created":

                str(datetime.now())

        }


        print(
            "[ZETA IMPLEMENTATION] Package ready"
        )


        return package
