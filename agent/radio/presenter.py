from datetime import datetime


class RadioPresenter:

    def __init__(self):

        self.name = "ZETA"

        self.style = "Warm Greek Cypriot storyteller"

        self.languages = [
            "English",
            "Greek",
            "Cypriot Greek"
        ]


    def create_intro(self, show="Morning Coffee"):

        intro = f"""
🎙️ Greek Roots Radio

Καλημέρα re koumbare!

Welcome to {show} on Greek Roots Radio.

Bringing you the sounds of Greece, Cyprus,
roots reggae and Mediterranean vibes.

From the villages of Cyprus
to the streets of London,
this is our culture, our memories,
and our music.

Stay with us — η παρέα μας μόλις ξεκινά!

Presented by {self.name}
"""

        return {
            "presenter": self.name,
            "show": show,
            "style": self.style,
            "content": intro,
            "created": str(datetime.now())
        }


if __name__ == "__main__":

    zeta = RadioPresenter()

    print(
        zeta.create_intro()
    )
