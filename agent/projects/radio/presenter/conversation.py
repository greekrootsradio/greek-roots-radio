from datetime import datetime


def create_transition(previous, next_track):

    script = f"""
Καλημέρα everyone!

That was {previous}.

You're listening to Greek Roots Radio with ZETA AI.

Bringing Greek Cypriot memories,
London community energy,
and Mediterranean sounds.

Coming next:

{next_track}.

Πάμε!
"""

    return {
        "presenter": "ZETA AI",
        "station": "Greek Roots Radio",
        "previous": previous,
        "next": next_track,
        "script": script,
        "style": [
            "Greek Cypriot warmth",
            "community radio",
            "friendly presenter"
        ],
        "created": datetime.now().isoformat()
    }


if __name__ == "__main__":

    result = create_transition(
        "Mia Fora",
        "Opa Cyprus"
    )

    print(result)
