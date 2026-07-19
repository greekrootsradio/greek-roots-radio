from datetime import datetime

from agent.projects.radio.intelligence.scheduler import create_schedule
from agent.projects.radio.music.intelligence.selector import select_music
from agent.projects.radio.voice.voice_engine import create_voice_intro
from agent.projects.radio.producer.show_brain import create_show_plan
from agent.projects.radio.director.broadcast_director import create_broadcast_decision


def create_live_broadcast():

    schedule = create_schedule()

    show = schedule["schedule"][0]

    music = select_music("festival")

    presenter = create_voice_intro()

    producer = create_show_plan()

    director = create_broadcast_decision()

    return {
        "engine": "ZETA Live Broadcast Controller",
        "station": "Greek Roots Radio",
        "time": str(datetime.now()),

        "show": show,

        "music": music,

        "presenter": presenter,

        "producer": producer,

        "director": director,

        "status": "LIVE_BROADCAST_READY"
    }


if __name__ == "__main__":

    broadcast = create_live_broadcast()

    print(broadcast)
