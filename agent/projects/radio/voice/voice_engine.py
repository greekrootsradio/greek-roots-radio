from datetime import datetime


def create_voice_intro(
    show="Morning Cyprus London"
):

    return {
        "station": "Greek Roots Radio",
        "presenter": "ZETA AI",
        "show": show,
        "intro": f"Welcome to {show} on Greek Roots Radio with ZETA AI",
        "style": [
            "Greek Cypriot warmth",
            "London community energy",
            "Mediterranean fusion"
        ],
        "voice": "not_connected",
        "created": str(datetime.now())
    }


if __name__ == "__main__":

    print(
        create_voice_intro()
    )

    print(
        {
            "engine": "ZETA Voice Presenter",
            "status": "ready_for_voice_provider",
            "presenter": "ZETA AI",
            "next": "generate_live_intro"
        }
    )
