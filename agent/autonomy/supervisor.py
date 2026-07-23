from agent.autonomy.logger import ZetaLogger
from agent.autonomy.self_inspector import SelfInspector
from agent.autonomy.development_cycle import DevelopmentCycle
from agent.autonomy.experience_engine import ExperienceEngine
from agent.autonomy.worker import ZetaWorker
from agent.autonomy.goal_orchestrator import GoalOrchestrator


class ZetaSupervisor:

    def __init__(self):

        self.logger = ZetaLogger()

        self.inspector = SelfInspector()

        self.development = DevelopmentCycle()

        self.experience = ExperienceEngine()

        self.worker = ZetaWorker()

        self.goal_orchestrator = GoalOrchestrator()

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
        # GOAL SELECTION
        #

        print(
            "[ZETA SUPERVISOR] Selecting next goal"
        )

        goal = self.goal_orchestrator.choose_goal()

        action = self.goal_orchestrator.create_action(goal)

        print(
            "[ZETA SUPERVISOR] Action:",
            action
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

        development_result = self.development.run()

        #
        # EXPERIENCE MEMORY
        #

        self.experience.record_cycle(
            {
                "module": "supervisor_cycle",
                "inspection": inspection,
                "goal": goal,
                "action": action,
                "worker": worker_result,
                "development": development_result,
                "result": "completed"
            }
        )

        print(
            "[ZETA SUPERVISOR] Cycle complete"
        )

        return {

            "inspection": inspection,

            "goal": goal,

            "action": action,

            "worker": worker_result,

            "development": development_result,

            "experience":
                self.experience.summarize()

        }


if __name__ == "__main__":

    supervisor = ZetaSupervisor()

    result = supervisor.run_cycle()

    print(result)
