from datetime import datetime

from agent.autonomy.health_monitor import HealthMonitor
from agent.autonomy.diagnostics import DiagnosticsAgent
from agent.autonomy.failure_memory import FailureMemory
from agent.autonomy.repair_history import RepairHistory
from agent.autonomy.repair_agent import RepairAgent
from agent.autonomy.git_manager import GitManagerAgent


class SupervisorAgent:

    def __init__(self):

        self.name = "ZETA Supervisor Agent"

        self.health = HealthMonitor()
        self.diagnostics = DiagnosticsAgent()
        self.failure_memory = FailureMemory()
        self.repair_history = RepairHistory()
        self.repair = RepairAgent()
        self.git = GitManagerAgent()


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
