from agent.autonomy.logger import ZetaLogger
from agent.autonomy.self_inspector import SelfInspector
from agent.autonomy.development_cycle import DevelopmentCycle
from agent.autonomy.experience_engine import ExperienceEngine


class ZetaSupervisor:

    def __init__(self):

        self.logger = ZetaLogger()
        self.inspector = SelfInspector()
        self.development = DevelopmentCycle()
        self.experience = ExperienceEngine()


    def run_cycle(self):

        print("[ZETA SUPERVISOR] Starting maintenance cycle")

        self.logger.write(
            "ZETA supervisor cycle started"
        )


        print("[ZETA SUPERVISOR] Inspecting system")

        inspection = self.inspector.inspect()


        print("[ZETA INSPECTOR]")
        print(inspection)


        print("[ZETA SUPERVISOR] Starting development cycle")


        self.development.run()


        self.experience.record_cycle(
            {
                "module": "supervisor_cycle",
                "result": "passed",
                "inspection_count": inspection.get(
                    "count",
                    0
                )
            }
        )


        print(
            "[ZETA SUPERVISOR] Cycle complete"
        )


        return {
            "inspection": inspection,
            "experience": self.experience.summarize()
        }
