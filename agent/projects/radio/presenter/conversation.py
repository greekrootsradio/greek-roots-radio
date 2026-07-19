from datetime import datetime


def create_presenter_message(
    previous_song,
    next_song,
    mood="morning"
):

    message = {
        "presenter": "ZETA AI",
        "station": "Greek Roots Radio",
        "mood": mood,
        "previous": previous_song,
        "next": next_song,
        "script": f"""
Καλημέρα everyone!

That was {previous_song}.

You're listening to Greek Roots Radio with ZETA AI.

Bringing Greek Cypriot memories,
London community energy,
and Mediterranean sounds.

Coming next:
{next_song}.

Πάμε!
""",
        "created": datetime.now().isoformat()
    }

    return message


if __name__ == "__main__":

    print(
        create_presenter_message(
            "Mia Fora",
            "Opa Cyprus"
        )
    )
