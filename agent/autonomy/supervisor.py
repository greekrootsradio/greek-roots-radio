import os
from datetime import datetime

from agent.autonomy.self_inspector import SelfInspector
from agent.autonomy.planner import PlannerAgent
from agent.autonomy.logger import ZetaLogger
from agent.autonomy.development_cycle import DevelopmentCycle
from agent.autonomy.learning_memory import LearningMemory


class ZetaSupervisor:

    def __init__(self):

        self.inspector = SelfInspector()
        self.planner = PlannerAgent()
        self.logger = ZetaLogger()
        self.development = DevelopmentCycle()
        self.memory = LearningMemory()


    def run_cycle(self):

        self.logger.log(
            "ZETA supervisor cycle started"
        )

        print(
            "\n[ZETA SUPERVISOR] Starting maintenance cycle\n"
        )


        # 1. Inspect herself

        inspection = self.inspector.inspect()


        # 2. Create improvement plan

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


        # 3. Build improvement proposal

        self.development.run()


        # 4. Store experience

        self.memory.remember(
            {
                "action": "completed supervisor development cycle",
                "build": plan["recommended_next_build"],
                "modules_found": inspection["count"],
                "result": "development cycle completed"
            }
        )


        print(
            "\n[ZETA SUPERVISOR] Cycle complete"
        )


        return {
            "inspection": inspection,
            "plan": plan,
            "memory": "updated"
        }
