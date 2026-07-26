from datetime import datetime

from agent.autonomy.health_monitor import HealthMonitor
from agent.autonomy.diagnostics import DiagnosticsAgent
from agent.autonomy.failure_memory import FailureMemory
from agent.autonomy.repair_history import RepairHistory
from agent.autonomy.repair_agent import RepairAgent
from agent.autonomy.git_manager import GitManagerAgent

from agent.radio.content_creator import ContentCreator


class ZetaSupervisor:

    def __init__(self):

        self.name = "ZETA Supervisor Agent"

        self.health = HealthMonitor()
        self.diagnostics = DiagnosticsAgent()
        self.failure_memory = FailureMemory()
        self.repair_history = RepairHistory()
        self.repair = RepairAgent()
        self.git = GitManagerAgent()

        # Greek Roots Radio autonomous creator
        self.content = ContentCreator()

    def run_check(self, failure=None):

        report = self.health.system_report()

        result = {
            "agent": self.name,
            "health": report,
            "created": str(datetime.now())
        }

        if failure:

            result["diagnostics"] = (
                self.diagnostics.analyse_failure(
                    failure
                )
            )

            result["memory"] = (
                self.failure_memory.record(
                    failure,
                    "queued investigation",
                    "pending"
                )
            )

            result["repair"] = (
                self.repair.propose_fix(
                    "unknown",
                    "prepare investigation proposal"
                )
            )

            result["git"] = (
                self.git.create_proposal(
                    "Supervisor investigation checkpoint"
                )
            )

        return result

    def run_cycle(self):

        print("\n==============================")
        print("ZETA SUPERVISOR CYCLE")
        print("==============================")

        report = self.run_check()

        print("✓ Health check complete")
        print(report)

        print("\nLaunching Greek Roots Radio mission...")

        content = self.content.create_daily_content()

        print("✓ Mission complete")
        print(content)

        return {
            "health": report,
            "mission": content
        }
