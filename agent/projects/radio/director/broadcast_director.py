from datetime import datetime


def create_broadcast_decision(
    show,
    track_style,
    mood
):

    decision = {

        "director": "ZETA AI",

        "station": "Greek Roots Radio",

        "show": show,

        "track": {
            "style": track_style,
            "mood": mood
        },

        "decisions": {

            "presenter_energy":
                "high" if mood == "festival"
                else "warm",

            "talk_length":
                "short" if track_style == "dance"
                else "medium",

            "add_context":
                True,

            "community_reference":
                True
        },

        "status": "broadcast_decision_ready",

        "created": datetime.now().isoformat()
    }


    return decision


if __name__ == "__main__":

    print(
        create_broadcast_decision(
            "Cyprus After Dark",
            "Mediterranean Reggae Fusion",
            "festival"
        )
    )
