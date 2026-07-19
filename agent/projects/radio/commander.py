import os
import datetime

from agent.projects.radio.controller import GreekRootsRadioController
from agent.projects.radio.stream import RadioStreamController
from agent.projects.radio.presenter.ai_presenter import AIPresenter
from agent.projects.radio.music.library import MusicLibrary


class RadioCommander:


    def __init__(self):

        self.log = os.path.expanduser(
            "~/cyprus/workspace/logs/zeta_radio_commander.log"
        )

        os.makedirs(
            os.path.dirname(self.log),
            exist_ok=True
        )

        self.controller = GreekRootsRadioController()
        self.stream = RadioStreamController()
        self.presenter = AIPresenter()
        self.music = MusicLibrary()



    def write(self, message):

        with open(self.log, "a") as f:

            f.write(
                f"{datetime.datetime.now()} {message}\n"
            )



    def assess_station(self):

        self.write(
            "Assessing station control state"
        )

        report = {

            "station": "Greek Roots Radio",

            "systems": {

                "controller": "available",

                "stream": "available",

                "presenter": "available",

                "music": "available"

            },

            "authority": "planning_only"

        }

        self.write(
            f"Assessment: {report}"
        )

        return report



    def execute_next_step(self):

        self.write(
            "Executive command evaluation"
        )

        command = {

            "action": "prepare_live_station",

            "stream": "standby",

            "presenter": "standby",

            "music": "standby",

            "approval_required": True

        }

        self.write(
            f"Command generated: {command}"
        )

        return command




if __name__ == "__main__":

    zeta_radio = RadioCommander()

    print(
        zeta_radio.assess_station()
    )

    print(
        zeta_radio.execute_next_step()
    )
