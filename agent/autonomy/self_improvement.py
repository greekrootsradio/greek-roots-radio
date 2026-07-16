import os
import json
from datetime import datetime


class SelfImprovementEngine:


    def __init__(self):

        self.history_file = os.path.expanduser(
            "~/cyprus/data/development_history.json"
        )


    def load_history(self):

        if not os.path.exists(self.history_file):

            return []


        with open(self.history_file, "r") as f:

            return json.load(f)



    def analyse(self):

        history = self.load_history()


        print("[ZETA IMPROVEMENT] Analysing experience")


        if not history:

            return {

                "status": "no_data",

                "recommendation": None

            }


        failures = []


        for event in history:

            if isinstance(event, dict):

                if event.get("status") == "failed":

                    failures.append(event)



        if failures:


            recommendation = {

                "type": "repair",

                "reason": "Repeated failures detected",

                "priority": 100

            }


        else:


            recommendation = {

                "type": "upgrade",

                "reason": "System operating normally",

                "priority": 50

            }



        result = {

            "time": str(datetime.now()),

            "history_events": len(history),

            "failures": len(failures),

            "recommendation": recommendation

        }


        print("[ZETA IMPROVEMENT] Result")

        print(result)


        return result
