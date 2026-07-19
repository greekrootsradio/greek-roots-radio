from datetime import datetime


def generate_voice_request(script):

    request = {
        "engine": "ZETA Voice Provider Bridge",
        "presenter": "ZETA AI",
        "station": "Greek Roots Radio",
        "script": script,
        "provider": "not_connected",
        "status": "ready_for_tts",
        "created": datetime.now().isoformat()
    }

    return request


if __name__ == "__main__":

    sample = """
    Καλημέρα everyone!
    You are listening to Greek Roots Radio with ZETA AI.
    """

    print(generate_voice_request(sample))
