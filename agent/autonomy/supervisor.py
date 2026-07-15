from agent.autonomy.self_inspector import SelfInspector
from agent.autonomy.planner import PlannerAgent
from agent.autonomy.logger import ZetaLogger
from agent.autonomy.development_cycle import DevelopmentCycle


class ZetaSupervisor:

    def __init__(self):

        self.inspector = SelfInspector()
        self.planner = PlannerAgent()
        self.development = DevelopmentCycle()
        self.logger = ZetaLogger()


    def run_cycle(self):

        self.logger.log(
            "ZETA supervisor cycle started"
        )

        print(
            "\n[ZETA SUPERVISOR] Starting maintenance cycle\n"
        )


        # 1. Inspect herself

        inspection = self.inspector.inspect()


        # 2. Decide next improvement

        plan = self.planner.analyse()


        self.logger.log(
            f"Inspection complete: {inspection['count']} modules found"
        )

        self.logger.log(
            f"Recommended build: {plan['recommended_next_build']}"
        )


        print(
            "\n[ZETA SUPERVISOR] Starting development cycle\n"
        )


        # 3. Controlled self improvement

        self.development.run()


        print(
            "\n[ZETA SUPERVISOR] Cycle complete"
        )


        return {
            "inspection": inspection,
            "plan": plan
        }
