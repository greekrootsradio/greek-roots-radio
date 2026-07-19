from datetime import datetime

from agent.projects.radio.live.controller import create_live_broadcast


def start_runtime():

    broadcast = create_live_broadcast()

    runtime = {

        "engine": "ZETA Radio Runtime Engine",

        "station": broadcast["station"],

        "started": datetime.now().isoformat(),

        "show": broadcast["producer"]["show"],

        "presenter": broadcast["presenter"]["presenter"],

        "next_track":
            broadcast["music"]["selected_tracks"][0]["title"],

        "status": "RADIO_RUNTIME_ACTIVE"

    }

    return runtime


if __name__ == "__main__":

    session = start_runtime()

    print(session)
