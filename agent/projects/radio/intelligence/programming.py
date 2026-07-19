from datetime import datetime


class RadioProgrammingIntelligence:

    def __init__(self):
        self.station = "Greek Roots Radio"

    def profile(self):

        return {
            "station": self.station,
            "format": "Greek Cypriot Mediterranean Fusion",
            "audience": "Greek Cypriots growing up in the UK",
            "style": [
                "Cypriot Greek",
                "Mediterranean",
                "Reggae fusion",
                "London culture"
            ],
            "mode": "creative_programming",
            "created": str(datetime.now())
        }


if __name__ == "__main__":

    intelligence = RadioProgrammingIntelligence()

    print(
        intelligence.profile()
    )
