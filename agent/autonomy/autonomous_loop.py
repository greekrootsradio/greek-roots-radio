import time

from agent.autonomy.supervisor import ZetaSupervisor


class AutonomousLoop:

    def __init__(self, sleep_seconds=300):

        self.sleep_seconds = sleep_seconds
        self.supervisor = ZetaSupervisor()

    def run_forever(self):

        print("[ZETA LOOP] Starting autonomous loop")

        while True:

            try:
                self.supervisor.run_cycle()

            except Exception as e:
                print(f"[ZETA LOOP] Cycle error: {e}")

            print(
                f"[ZETA LOOP] Sleeping for {self.sleep_seconds} seconds"
            )

            time.sleep(self.sleep_seconds)
