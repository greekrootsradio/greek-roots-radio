from datetime import datetime

from agent.projects.radio.intelligence.scheduler import RadioProgrammingScheduler
from agent.projects.radio.controller import GreekRootsRadioController
from agent.projects.radio.presenter.ai_presenter import AIPresenter
from agent.projects.radio.music.library import MusicLibrary


class LiveShowEngine:

    def __init__(self):

        self.station = "Greek Roots Radio"

        self.scheduler = RadioProgrammingScheduler()
        self.controller = GreekRootsRadioController()
        self.presenter = AIPresenter()
        self.music = MusicLibrary()


    def prepare_show(self):

        schedule = self.scheduler.create_schedule()

        return {
            "station": self.station,
            "engine": "ZETA Live Show Orchestrator",
            "time": str(datetime.now()),
            "status": "preparing",

            "systems": {
                "controller": "ready",
                "scheduler": "ready",
                "presenter": "ready",
                "music": "ready"
            },

            "next_show": schedule["schedule"][0]
        }


    def run_cycle(self):

        return {
            "show_engine": self.prepare_show(),
            "decision": "awaiting_stream_authorisation"
        }


if __name__ == "__main__":

    engine = LiveShowEngine()

    print(
        engine.run_cycle()
    )
