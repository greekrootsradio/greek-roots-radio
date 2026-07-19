from datetime import datetime


def create_show_plan(
    show,
    mood,
    audience
):

    plan = {
        "producer": "ZETA AI",
        "station": "Greek Roots Radio",
        "show": show,
        "mood": mood,
        "audience": audience,

        "presenter_rules": {
            "talk_frequency": "between major tracks",
            "tone": "warm Greek Cypriot community",
            "language": [
                "English",
                "Cypriot Greek phrases"
            ],
            "humour": "friendly"
        },

        "content": {
            "community_mentions": True,
            "music_context": True,
            "artist_information": True
        },

        "status": "show_plan_ready",
        "created": datetime.now().isoformat()
    }

    return plan


if __name__ == "__main__":

    print(
        create_show_plan(
            "Morning Cyprus London",
            "sunrise Mediterranean",
            "Greek Cypriots growing up in the UK"
        )
    )
