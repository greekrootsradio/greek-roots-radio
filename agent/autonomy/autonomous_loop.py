from agent.autonomy.supervisor import ZetaSupervisor
from agent.autonomy.upgrader import UpgradeManager
from agent.autonomy.logger import ZetaLogger


class AutonomousLoop:

    def __init__(self):

        self.supervisor = ZetaSupervisor()
        self.upgrader = UpgradeManager()
        self.logger = ZetaLogger()


    def run(self):

        self.logger.write(
            "Autonomous loop started"
        )

        report = self.supervisor.run_cycle()


        idea = report["plan"]["recommended_next_build"]


        proposal = self.upgrader.propose(
            f"Build and improve {idea} module"
        )


        self.logger.write(
            f"New upgrade proposal created: {idea}"
        )


        return proposal
