import time
from datetime import datetime

from agent.autonomy.supervisor import ZetaSupervisor


class AutonomyOrchestrator:

    def __init__(self):

        self.supervisor = ZetaSupervisor()

        self.running = False


    def start(self):

        self.running = True

        print("ZETA AUTONOMY ORCHESTRATOR ONLINE")

        while self.running:

            try:

                self.run_cycle()

            except Exception as e:

                print("Autonomy cycle error:")
                print(e)

            time.sleep(300)


    def run_cycle(self):

        print()
        print("================================")
        print("ZETA AUTONOMY CYCLE")
        print(datetime.now())
        print("================================")

        result = self.supervisor.run_cycle()

        print()
        print("CYCLE COMPLETE")
        print(result)

        return result


    def stop(self):

        self.running = False

        print("ZETA AUTONOMY ORCHESTRATOR STOPPED")
