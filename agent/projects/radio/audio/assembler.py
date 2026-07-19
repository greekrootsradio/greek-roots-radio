from datetime import datetime


def assemble_segment():

    segment = {

        "engine": "ZETA Audio Assembly Engine",

        "station": "Greek Roots Radio",

        "show": "Morning Cyprus London",

        "voice": {

            "presenter": "ZETA AI",

            "status": "VOICE_READY"

        },

        "music": {

            "track": "Opa Cyprus",

            "artist": "Traditional Cyprus"

        },

        "mix": {

            "intro_before_music": True,

            "crossfade": True,

            "volume_balance": "automatic"

        },

        "status": "AUDIO_SEGMENT_READY",

        "created": datetime.now().isoformat()

    }


    return segment


if __name__ == "__main__":

    print(assemble_segment())
