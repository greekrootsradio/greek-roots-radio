from datetime import datetime


def select_music(request="festival"):

    return {
        "station": "Greek Roots Radio",
        "request": request,
        "selected_tracks": [
            {
                "artist": "Traditional Cyprus",
                "title": "Opa Cyprus",
                "style": "mediterranean",
                "mood": request
            }
        ],
        "count": 1,
        "created": str(datetime.now())
    }


if __name__ == "__main__":
    print(select_music())
