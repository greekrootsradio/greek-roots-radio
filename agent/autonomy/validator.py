from datetime import datetime


class Validator:


    def __init__(self):

        self.name = "ZETA Validator"



    def validate(self, execution_package):

        print(
            "[ZETA VALIDATOR] Checking execution package"
        )


        checks = {

            "proposal_present":
                bool(
                    execution_package.get(
                        "task"
                    )
                ),

            "build_plan_present":
                bool(
                    execution_package.get(
                        "build_plan"
                    )
                ),

            "test_plan_present":
                bool(
                    execution_package.get(
                        "test_plan"
                    )
                ),

            "execution_permission":
                execution_package.get(
                    "execution_allowed",
                    False
                )

        }


        approved = all(
            checks.values()
        )


        result = {

            "validator": self.name,

            "task":
                execution_package.get(
                    "task"
                ),

            "checks":
                checks,

            "validated":
                approved,

            "reason":

                "ready for execution"
                if approved
                else
                "approval or requirements missing",

            "time":
                str(datetime.now())

        }


        print(
            "[ZETA VALIDATOR] Complete"
        )


        return result
