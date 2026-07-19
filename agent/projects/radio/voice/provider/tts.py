from datetime import datetime


def generate_voice(script):

    return {

        "engine": "ZETA TTS Bridge",

        "presenter": "ZETA AI",

        "station": "Greek Roots Radio",

        "script": script,

        "provider": "pending",

        "audio_file": None,

        "status": "VOICE_REQUEST_READY",

        "created": datetime.now().isoformat()

    }


if __name__ == "__main__":

    test = generate_voice(
        "Καλημέρα everyone. Welcome to Greek Roots Radio with ZETA AI."
    )

    print(test)
