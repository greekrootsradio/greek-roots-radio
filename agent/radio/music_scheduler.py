import random
from datetime import datetime


class MusicScheduler:

    def __init__(self):

        self.station = "Greek Roots Radio"

        self.library = {

            "Greek Classics": [
                "Mikis Theodorakis",
                "Manolis Angelopoulos",
                "Glykeria"
            ],

            "Cypriot": [
                "Cypriot Traditional",
                "Laiko Cyprus",
                "Island Folk"
            ],

            "Reggae": [
                "Bob Marley",
                "Roots Reggae",
                "Dub Culture"
            ],

            "Mediterranean Fusion": [
                "Greek Reggae Fusion",
                "Bouzouki Beats",
                "Mediterranean Groove"
            ]

        }


    def create_playlist(self):

        playlist = []

        categories = list(self.library.keys())

        for i in range(10):

            category = random.choice(categories)

            song_style = random.choice(
                self.library[category]
            )

            playlist.append({

                "position": i + 1,

                "category": category,

                "selection": song_style

            })


        return {

            "station": self.station,

            "playlist": playlist,

            "created": str(datetime.now()),

            "status": "playlist generated"

        }


if __name__ == "__main__":

    scheduler = MusicScheduler()

    print(
        scheduler.create_playlist()
    )
