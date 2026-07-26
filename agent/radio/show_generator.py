from datetime import datetime


class ShowGenerator:

    def __init__(self):

        self.agent = "ZETA Radio Show Generator"

        self.station = "Greek Roots Radio"


    def create_show(self, show_name="Morning Coffee"):

        show = {

            "station": self.station,

            "show": show_name,

            "presenter": {

                "name": "ZETA",

                "style": "Warm Greek Cypriot storyteller",

                "languages": [
                    "English",
                    "Greek",
                    "Cypriot Greek"
                ]

            },


            "segments": [

                {
                    "time": "00:00",
                    "title": "Opening Welcome",
                    "content":
                    "Καλημέρα re koumbare! Welcome to Greek Roots Radio."
                },


                {
                    "time": "00:05",
                    "title": "Greek Roots Music",
                    "content":
                    "Classic Greek, Cyprus sounds and Mediterranean vibes."
                },


                {
                    "time": "00:20",
                    "title": "Reggae Connection",
                    "content":
                    "Roots reggae and island rhythms from around the world."
                },


                {
                    "time": "00:45",
                    "title": "Community Story",
                    "content":
                    "Stories from Greek Cypriots growing up in the UK."
                }

            ],


            "closing":

            """
            Efharisto for listening.

            Keep the music alive.
            Keep the roots alive.

            This is ZETA on Greek Roots Radio.
            """,


            "created":

            str(datetime.now())

        }


        return show



if __name__ == "__main__":

    z = ShowGenerator()

    print(z.create_show())
