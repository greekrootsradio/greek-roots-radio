from datetime import datetime

from agent.projects.radio.brain.station_brain import station_decision


def start_runtime():

    brain = station_decision()

    runtime = {

        "engine": "ZETA Intelligent Radio Runtime",

        "station": "Greek Roots Radio",

        "started": datetime.now().isoformat(),

        "brain": brain,

        "show": brain["show"],

        "mood": brain["mood"],

        "presenter": "ZETA AI",

        "status": "INTELLIGENT_RUNTIME_ACTIVE"

    }

    return runtime


if __name__ == "__main__":

    print(start_runtime())
