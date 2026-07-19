import os
import datetime


class GreekRootsRadioManager:


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


    def check_status(self):

        self.write(
            "Checking Greek Roots Radio status"
        )

        status = {
            "station": "Greek Roots Radio",
            "stream": "offline",
            "playlist": "not_loaded",
            "presenter": "not_active"
        }


        self.write(
            f"Radio status: {status}"
        )

        return status



    def plan_next_action(self):

        self.write(
            "Planning next radio action"
        )

        action = {
            "action": "prepare station startup",
            "priority": 1
        }


        self.write(
            f"Next action: {action}"
        )

        return action



if __name__ == "__main__":

    radio = GreekRootsRadioManager()

    print(
        radio.check_status()
    )

    print(
        radio.plan_next_action()
    )
