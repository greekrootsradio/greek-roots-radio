from datetime import datetime


def create_schedule():

    return {
        "station": "Greek Roots Radio",
        "date": str(datetime.now()),
        "schedule": [
            {
                "time": "06:00",
                "show": "Morning Cyprus London",
                "mood": "sunrise Mediterranean",
                "music": [
                    "Cypriot Greek",
                    "Laiko",
                    "Mediterranean fusion"
                ],
                "presenter": "ZETA AI"
            },
            {
                "time": "12:00",
                "show": "Greek Roots Midday",
                "mood": "community energy",
                "music": [
                    "Greek classics",
                    "Reggae fusion",
                    "London Cyprus vibes"
                ],
                "presenter": "ZETA AI"
            },
            {
                "time": "18:00",
                "show": "Cyprus After Dark",
                "mood": "festival club energy",
                "music": [
                    "Bouzouki",
                    "Afro Mediterranean",
                    "Dance fusion"
                ],
                "presenter": "ZETA AI"
            }
        ]
    }


if __name__ == "__main__":
    print(create_schedule())
