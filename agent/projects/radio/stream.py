import os
import datetime


class RadioStreamController:


    def __init__(self):

        self.log = os.path.expanduser(
            "~/cyprus/workspace/logs/greek_roots_radio.log"
        )

        os.makedirs(
            os.path.dirname(self.log),
            exist_ok=True
        )

        self.stream_state = "offline"



    def write(self, message):

        with open(self.log, "a") as f:

            f.write(
                f"{datetime.datetime.now()} {message}\n"
            )



    def status(self):

        self.write(
            "Checking stream status"
        )

        result = {
            "stream": self.stream_state,
            "engine": "not_configured"
        }

        self.write(
            f"Stream status: {result}"
        )

        return result



    def prepare(self):

        self.write(
            "Preparing stream engine"
        )

        result = {
            "action": "prepare_stream",
            "status": "ready_for_engine"
        }

        self.write(
            f"Stream preparation: {result}"
        )

        return result



    def start(self):

        self.write(
            "Start command received"
        )

        self.stream_state = "online"

        result = {
            "stream": "online",
            "status": "started"
        }

        self.write(
            f"Stream started: {result}"
        )

        return result



    def stop(self):

        self.write(
            "Stop command received"
        )

        self.stream_state = "offline"

        result = {
            "stream": "offline",
            "status": "stopped"
        }

        self.write(
            f"Stream stopped: {result}"
        )

        return result



if __name__ == "__main__":

    stream = RadioStreamController()

    print(
        stream.status()
    )

    print(
        stream.prepare()
    )

    print(
        stream.start()
    )
