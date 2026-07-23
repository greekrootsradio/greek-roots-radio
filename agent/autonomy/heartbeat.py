import time
from datetime import datetime

from agent.autonomy.supervisor import ZetaSupervisor


class ZetaHeartbeat:


    def __init__(self):

        self.supervisor = ZetaSupervisor()

        self.running = True


    def start(self):

        print(
            "[ZETA HEARTBEAT] Starting autonomous mode"
        )


        while self.running:

            try:

                print(
                    "\n[ZETA HEARTBEAT]",
                    datetime.now()
                )


                result = self.supervisor.run_cycle()


                print(
                    "[ZETA HEARTBEAT] Cycle finished"
                )


            except Exception as e:

                print(
                    "[ZETA HEARTBEAT ERROR]",
                    e
                )


            print(
                "[ZETA HEARTBEAT] Sleeping 60 seconds"
            )


            time.sleep(60)



if __name__ == "__main__":

    heartbeat = ZetaHeartbeat()

    heartbeat.start()
