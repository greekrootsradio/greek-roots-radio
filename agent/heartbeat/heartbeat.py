import time
from datetime import datetime

from agent.executive.executive_cycle import ExecutiveCycle


class ZetaHeartbeat:

    def __init__(self):

        self.name = "ZETA Heartbeat"
        self.executive = ExecutiveCycle()


    def pulse(self):

        print()
        print("==============================")
        print("ZETA HEARTBEAT")
        print("==============================")

        result = {

            "agent": self.name,

            "heartbeat":

                str(datetime.now()),

            "status":

                "awake"

        }


        print("✓ Heartbeat active")

        print()
        print("Running executive cycle...")
        

        cycle_result = self.executive.cycle()


        result["executive_cycle"] = cycle_result


        print()
        print("✓ Executive cycle completed")

        return result



    def run_once(self):

        return self.pulse()



    def run_forever(self, interval=300):

        print("ZETA heartbeat service started")

        while True:

            try:

                self.pulse()


            except Exception as error:

                print(
                    "Heartbeat error:",
                    error
                )


            time.sleep(interval)
