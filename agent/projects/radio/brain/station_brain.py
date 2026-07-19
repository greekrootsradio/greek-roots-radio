from datetime import datetime


def station_decision():

    hour = datetime.now().hour


    if hour < 12:

        mood = "sunrise Mediterranean energy"

        show = "Morning Cyprus London"

    elif hour < 18:

        mood = "community afternoon"

        show = "Cyprus London Drive"

    else:

        mood = "festival evening energy"

        show = "Cyprus After Dark"


    decision = {

        "brain": "ZETA Real-Time Station Brain",

        "station": "Greek Roots Radio",

        "time": datetime.now().isoformat(),

        "show": show,

        "mood": mood,

        "decisions": {

            "change_show": True,

            "adapt_music": True,

            "adapt_presenter_energy": True,

            "community_mode": True

        },

        "status": "STATION_DECISION_READY"

    }


    return decision


if __name__ == "__main__":

    print(station_decision())
