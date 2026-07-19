from datetime import datetime

from agent.projects.radio.brain.station_brain import station_decision
from agent.projects.radio.live.runtime.engine import start_runtime
from agent.projects.radio.audio.assembler import assemble_segment


def start_station():

    brain = station_decision()

    runtime = start_runtime()

    audio = assemble_segment()


    station = {

        "engine": "ZETA Autonomous Radio Host",

        "station": "Greek Roots Radio",

        "started": datetime.now().isoformat(),

        "brain": brain,

        "runtime": runtime,

        "audio": audio,

        "status": "GREEK_ROOTS_RADIO_ONLINE"

    }


    return station


if __name__ == "__main__":

    print(start_station())
