import os
import sys
import datetime


BASE_DIR = os.path.expanduser("~/cyprus")

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)


from agent.projects.radio.controller import GreekRootsRadioController



class ZetaRadioAutopilot:


    def __init__(self):

        self.log = os.path.expanduser(
            "~/cyprus/workspace/logs/zeta_radio_autopilot.log"
        )

        os.makedirs(
            os.path.dirname(self.log),
            exist_ok=True
        )

        self.station = GreekRootsRadioController()



    def write(self, message):

        with open(self.log, "a") as f:
            f.write(
                f"{datetime.datetime.now()} {message}\n"
            )



    def think(self):

        self.write(
            "=== ZETA RADIO AUTOPILOT THINK CYCLE ==="
        )


        status = self.station.startup_check()


        decision = {

            "station": "Greek Roots Radio",

            "health": "checked",

            "decision": "prepare_station"

        }


        self.write(
            f"Decision: {decision}"
        )


        return decision



    def execute(self):

        self.write(
            "Executing radio preparation"
        )


        result = self.station.prepare_station()


        self.write(
            f"Execution result: {result}"
        )


        return result



if __name__ == "__main__":


    autopilot = ZetaRadioAutopilot()


    print(
        autopilot.think()
    )


    print(
        autopilot.execute()
    )
