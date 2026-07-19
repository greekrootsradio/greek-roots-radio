from datetime import datetime


class MusicIntelligence:

    def __init__(self):

        self.station = "Greek Roots Radio"

        self.library = [
            {
                "artist": "Traditional Cyprus",
                "title": "Opa Cyprus",
                "style": "mediterranean",
                "mood": "festival"
            },
            {
                "artist": "Greek Roots",
                "title": "London Cyprus Vibes",
                "style": "reggae fusion",
                "mood": "community"
            },
            {
                "artist": "Cyprus Laiko",
                "title": "Island Nights",
                "style": "laiko",
                "mood": "evening"
            }
        ]


    def select_music(self, mood):

        matches = []

        for track in self.library:

            if track["mood"] == mood:
                matches.append(track)

        return {
            "station": self.station,
            "request": mood,
            "selected_tracks": matches,
            "count": len(matches),
            "created": str(datetime.now())
        }


    def create_playlist(self, show):

        return {
            "show": show,
            "playlist_engine": "ZETA Music Intelligence",
            "status": "ready",
            "next_action": "match_music_to_show"
        }


if __name__ == "__main__":

    music = MusicIntelligence()

    print(
        music.select_music(
            "festival"
        )
    )

    print(
        music.create_playlist(
            "Cyprus After Dark"
        )
    )
