from datetime import datetime

from agent.projects.radio.producer.show_brain import create_show_plan
from agent.projects.radio.director.broadcast_director import create_broadcast_decision
from agent.projects.radio.music.intelligence.selector import select_music
from agent.projects.radio.voice.voice_engine import create_voice_intro
from agent.projects.radio.presenter.conversation import create_transition


def create_live_broadcast():

    station = "Greek Roots Radio"

    show = "Morning Cyprus London"
    mood = "sunrise Mediterranean"
    audience = "Greek Cypriots growing up in the UK"

    producer = create_show_plan(
        show,
        mood,
        audience
    )

    music = select_music(
        "festival"
    )

    track_style = music["selected_tracks"][0]["style"]

    director = create_broadcast_decision(
        show,
        track_style,
        mood
    )

    voice = create_voice_intro(
        show
    )

    presenter = create_transition(
        "Mia Fora",
        "Opa Cyprus"
    )

    return {
        "engine": "ZETA Live Broadcast Controller",
        "station": station,
        "time": datetime.now().isoformat(),

        "producer": producer,
        "music": music,
        "director": director,
        "voice": voice,
        "presenter": presenter,

        "status": "LIVE_BROADCAST_READY"
    }


if __name__ == "__main__":

    broadcast = create_live_broadcast()

    print(broadcast)
