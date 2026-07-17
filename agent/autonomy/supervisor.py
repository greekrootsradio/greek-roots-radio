from agent.autonomy.logger import ZetaLogger
from agent.autonomy.self_inspector import SelfInspector
from agent.autonomy.development_cycle import DevelopmentCycle
from agent.autonomy.experience_engine import ExperienceEngine
from agent.autonomy.worker import ZetaWorker


class ZetaSupervisor:


    def __init__(self):

        self.logger = ZetaLogger()

        self.inspector = SelfInspector()

        self.development = DevelopmentCycle()

        self.experience = ExperienceEngine()

        self.worker = ZetaWorker()



    def run_cycle(self):

        print(
            "[ZETA SUPERVISOR] Starting autonomous cycle"
        )


        self.logger.write(
            "Supervisor autonomous cycle started"
        )



        #
        # SYSTEM INSPECTION
        #

        print(
            "[ZETA SUPERVISOR] Inspecting system"
        )


        inspection = self.inspector.inspect()


        print(
            "[ZETA INSPECTOR]",
            inspection
        )



        #
        # TASK EXECUTION
        #

        print(
            "[ZETA SUPERVISOR] Running worker"
        )


        worker_result = self.worker.run_once()



        #
        # DEVELOPMENT MAINTENANCE
        #

        print(
            "[ZETA SUPERVISOR] Running development maintenance"
        )


        self.development.run()



        #
        # EXPERIENCE MEMORY
        #

        self.experience.record_cycle(
            {
                "module": "supervisor_cycle",

                "inspection": inspection,

                "worker": worker_result,

                "result": "completed"
            }
        )



        print(
            "[ZETA SUPERVISOR] Cycle complete"
        )


        return {

            "inspection": inspection,

            "worker": worker_result,

            "experience":
                self.experience.summarize()

        }
