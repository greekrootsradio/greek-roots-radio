from datetime import datetime


class ZetaVoiceEngine:

    def __init__(self):

        self.station = "Greek Roots Radio"
        self.presenter = "ZETA AI"
        self.voice_state = "not_connected"


    def create_intro(self, show):

        return {
            "station": self.station,
            "presenter": self.presenter,
            "show": show,
            "intro": f"Welcome to {show} on Greek Roots Radio with ZETA AI",
            "style": [
                "Greek Cypriot warmth",
                "London community energy",
                "Mediterranean fusion"
            ],
            "voice": self.voice_state,
            "created": str(datetime.now())
        }


    def prepare_voice_job(self):

        return {
            "engine": "ZETA Voice Presenter",
            "status": "ready_for_voice_provider",
            "presenter": self.presenter,
            "next": "generate_live_intro"
        }


if __name__ == "__main__":

    voice = ZetaVoiceEngine()

    print(
        voice.create_intro(
            "Morning Cyprus London"
        )
    )

    print(
        voice.prepare_voice_job()
    )
