import os
import datetime


class MusicLibrary:


    def __init__(self):

        self.log = os.path.expanduser(
            "~/cyprus/workspace/logs/greek_roots_radio.log"
        )

        os.makedirs(
            os.path.dirname(self.log),
            exist_ok=True
        )

        self.library = []



    def write(self, message):

        with open(self.log, "a") as f:
            f.write(
                f"{datetime.datetime.now()} {message}\n"
            )



    def status(self):

        result = {
            "music_library": "connected",
            "tracks": len(self.library)
        }

        self.write(
            f"Music status: {result}"
        )

        return result



    def add_track(self, artist, title, style):

        track = {
            "artist": artist,
            "title": title,
            "style": style
        }

        self.library.append(track)

        self.write(
            f"Track added: {track}"
        )

        return track



    def build_playlist(self, mood="mediterranean"):

        playlist = [
            track for track in self.library
            if track["style"] == mood
        ]

        result = {
            "playlist": playlist,
            "count": len(playlist)
        }

        self.write(
            f"Playlist generated: {result}"
        )

        return result



if __name__ == "__main__":

    music = MusicLibrary()

    music.add_track(
        "Traditional Cyprus",
        "Opa Cyprus",
        "mediterranean"
    )

    music.add_track(
        "Greek Roots",
        "London Cyprus Vibes",
        "mediterranean"
    )

    print(
        music.status()
    )

    print(
        music.build_playlist()
    )
