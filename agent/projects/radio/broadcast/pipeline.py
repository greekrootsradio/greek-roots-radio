from datetime import datetime

from agent.projects.radio.intelligence.scheduler import create_schedule
from agent.projects.radio.music.intelligence.selector import select_music
from agent.projects.radio.voice.voice_engine import create_voice_intro


def build_broadcast():

    schedule = create_schedule()

    next_show = schedule["schedule"][0]

    music = select_music("festival")

    voice = create_voice_intro(
        next_show["show"]
    )

    broadcast = {
        "station": "Greek Roots Radio",
        "engine": "ZETA Autonomous Broadcast Pipeline",
        "time": str(datetime.now()),

        "show": next_show,

        "music": music,

        "voice": voice,

        "status": "broadcast_package_ready"
    }

    return broadcast


if __name__ == "__main__":
    print(build_broadcast())
