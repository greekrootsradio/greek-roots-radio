import time
from datetime import datetime

from agent.autonomy.supervisor import ZetaSupervisor


class AutonomyEngine:

    def __init__(self, sleep_seconds=300):

        self.sleep_seconds = sleep_seconds
        self.supervisor = ZetaSupervisor()

        self.running = False

    def start(self):

        self.running = True

        print("[ZETA ENGINE] Online")

        while self.running:

            try:

                self.supervisor.run_cycle()

            except Exception as e:

                print(f"[ZETA ENGINE] Error: {e}")

            print(
                f"[ZETA ENGINE] Sleeping {self.sleep_seconds} seconds"
            )

            time.sleep(self.sleep_seconds)

    def stop(self):

        self.running = False

        print("[ZETA ENGINE] Stopped")


if __name__ == "__main__":

    engine = AutonomyEngine(sleep_seconds=10)

    engine.start()
