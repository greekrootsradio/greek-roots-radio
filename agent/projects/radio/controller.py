import os
import sys
import datetime


BASE_DIR = os.path.expanduser("~/cyprus")

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)


from agent.projects.radio.manager import GreekRootsRadioManager
from agent.projects.radio.stream import RadioStreamController
from agent.projects.radio.presenter.ai_presenter import AIPresenter
from agent.projects.radio.music.library import MusicLibrary



class GreekRootsRadioController:


    def __init__(self):

        self.log = os.path.expanduser(
            "~/cyprus/workspace/logs/greek_roots_radio.log"
        )

        os.makedirs(
            os.path.dirname(self.log),
            exist_ok=True
        )

        self.radio = GreekRootsRadioManager()
        self.stream = RadioStreamController()
        self.presenter = AIPresenter()
        self.music = MusicLibrary()



    def write(self, message):

        with open(self.log, "a") as f:
            f.write(
                f"{datetime.datetime.now()} {message}\n"
            )



    def startup_check(self):

        self.write(
            "=== ZETA RADIO AUTONOMOUS STARTUP CHECK ==="
        )

        result = {

            "station": self.radio.check_status(),

            "stream": self.stream.status(),

            "presenter": self.presenter.status(),

            "music": self.music.status()

        }

        self.write(
            f"Startup report: {result}"
        )

        return result



    def prepare_station(self):

        self.write(
            "Preparing Greek Roots Radio"
        )

        result = {

            "stream": self.stream.prepare(),

            "show": self.presenter.prepare_show(),

            "playlist": self.music.build_playlist()

        }

        self.write(
            f"Station preparation complete: {result}"
        )

        return result



if __name__ == "__main__":

    station = GreekRootsRadioController()


    print(
        station.startup_check()
    )


    print(
        station.prepare_station()
    )
