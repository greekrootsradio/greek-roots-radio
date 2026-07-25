import json
import os
from datetime import datetime


class DecisionEngine:

    def __init__(self):

        self.name = "ZETA Decision Engine"

        self.file = os.path.expanduser(
            "~/cyprus/workspace/decision_history.json"
        )

        os.makedirs(
            os.path.dirname(self.file),
            exist_ok=True
        )

        if not os.path.exists(self.file):

            with open(self.file, "w") as f:
                json.dump([], f, indent=4)


    def _load(self):

        with open(self.file, "r") as f:
            return json.load(f)


    def _save(self, data):

        with open(self.file, "w") as f:
            json.dump(
                data,
                f,
                indent=4
            )


    def evaluate(
        self,
        situation,
        options
    ):

        decision = {

            "agent":
                self.name,

            "situation":
                situation,

            "options":
                options,

            "recommendation":
                options[0] if options else None,

            "status":
                "awaiting approval",

            "created":
                str(datetime.now())

        }


        history = self._load()

        history.append(decision)

        self._save(history)

        return decision


    def history(self):

        return self._load()
