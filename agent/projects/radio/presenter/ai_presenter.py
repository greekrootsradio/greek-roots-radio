import os
import datetime


class AIPresenter:


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



    def status(self):

        result = {
            "presenter": "ZETA AI Host",
            "state": "offline",
            "voice": "not_configured"
        }

        self.write(
            f"Presenter status: {result}"
        )

        return result



    def prepare_show(self):

        result = {
            "action": "prepare_live_show",
            "host": "ZETA AI",
            "status": "ready"
        }

        self.write(
            f"Show preparation: {result}"
        )

        return result



if __name__ == "__main__":

    host = AIPresenter()

    print(host.status())

    print(host.prepare_show())
