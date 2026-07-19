from datetime import datetime


def create_transition(previous_track, next_track, mood):

    transition = {

        "presenter": "ZETA AI",

        "transition": {
            "from": previous_track,
            "to": next_track,
            "mood": mood
        },

        "script": (
            f"That was {previous_track}. "
            f"You're listening to Greek Roots Radio. "
            f"Coming next, we bring you {next_track} "
            f"with that Mediterranean London energy."
        ),

        "style": [
            "Greek Cypriot warmth",
            "community radio",
            "friendly presenter"
        ],

        "created": str(datetime.now())
    }

    return transition


if __name__ == "__main__":

    print(
        create_transition(
            "Traditional Cyprus Classic",
            "Mediterranean Reggae Fusion",
            "festival"
        )
    )
