import os
import sys

BASE_DIR = os.path.expanduser("~/cyprus")

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)


from agent.projects.radio.manager import GreekRootsRadioManager


class ExecutiveAction:


    def __init__(self):

        self.radio = GreekRootsRadioManager()


    def execute(self, goal):

        if goal["name"] == "Keep Greek Roots Radio online":

            status = self.radio.check_status()

            action = self.radio.plan_next_action()

            return {
                "status": status,
                "action": action
            }


        return {
            "status": "no action"
        }



if __name__ == "__main__":

    executor = ExecutiveAction()

    print(
        executor.execute(
            {
                "name": "Keep Greek Roots Radio online"
            }
        )
    )
