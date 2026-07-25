import os
from datetime import datetime

from agent.memory.memory_guardian import MemoryGuardian
from agent.autonomy.improvement_planner import ImprovementPlanner
from agent.autonomy.repair_executor import RepairExecutor


class ExecutiveCycle:

    def __init__(self):

        self.name = "ZETA Executive Cycle"

        self.memory_file = os.path.expanduser(
            "~/cyprus/data/memory.json"
        )

        self.guardian = MemoryGuardian()

        self.planner = ImprovementPlanner()

        self.repair = RepairExecutor()


    def cycle(self):

        print()
        print("==============================")
        print("ZETA EXECUTIVE CYCLE")
        print("==============================")


        report = {

            "agent": self.name,

            "started":
                str(datetime.now())

        }


        # 1. Memory health

        try:

            report["memory"] = self.guardian.monitor()

            print("✓ Memory checked")

        except Exception as e:

            report["memory_error"] = str(e)



        # 2. Self improvement planning

        try:

            plan = self.planner.create_plan(

                "Review current ZETA behaviour",

                "Improve reliability and autonomy"

            )

            report["planner"] = plan

            print("✓ Improvement plan created")


        except Exception as e:

            report["planner_error"] = str(e)



        # 3. Prepare repair / improvement action

        try:

            repair = self.repair.execute(

                "Improve ZETA reliability"

            )

            report["repair"] = repair

            print("✓ Repair task prepared")


        except Exception as e:

            report["repair_error"] = str(e)



        # 4. Validate cycle

        try:

            validation = self.repair.validate(

                "Executive cycle",

                "Executive cycle completed successfully"

            )

            report["validation"] = validation

            print("✓ Validation complete")


        except Exception as e:

            report["validation_error"] = str(e)



        report["finished"] = str(datetime.now())


        return report
