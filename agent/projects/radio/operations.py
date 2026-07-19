import os
import datetime


class RadioOperations:


    def __init__(self):

        self.log = os.path.expanduser(
            "~/cyprus/workspace/logs/greek_roots_radio.log"
        )

        os.makedirs(
            os.path.dirname(self.log),
            exist_ok=True
        )


    def write(self, message):

        with open(self.log, "a") as f:

            f.write(
                f"{datetime.datetime.now()} {message}\n"
            )


    def startup_check(self):

        self.write(
            "Running radio startup check"
        )

        checks = {
            "stream_engine": "not_configured",
            "music_library": "not_connected",
            "playlist": "empty",
            "ai_presenter": "offline"
        }

        self.write(
            f"Startup check: {checks}"
        )

        return checks



    def prepare_station(self):

        self.write(
            "Preparing Greek Roots Radio startup"
        )

        return {
            "action": "prepare_station",
            "status": "ready_for_configuration"
        }



if __name__ == "__main__":

    radio = RadioOperations()

    print(
        radio.startup_check()
    )

    print(
        radio.prepare_station()
    )
