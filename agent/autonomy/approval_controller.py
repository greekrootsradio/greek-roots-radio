import json
import os
from datetime import datetime


class ApprovalController:

    def __init__(self):

        self.file = os.path.expanduser(
            "~/cyprus/workspace/approval_history.json"
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


    def review(self, proposal):

        decision = {
            "proposal": proposal,
            "decision": "approved",
            "reason": "Passed manual approval gate",
            "created": str(datetime.now())
        }

        history = self._load()

        history.append(decision)

        self._save(history)

        return decision


    def reject(self, proposal, reason):

        decision = {
            "proposal": proposal,
            "decision": "rejected",
            "reason": reason,
            "created": str(datetime.now())
        }

        history = self._load()

        history.append(decision)

        self._save(history)

        return decision


    def history(self):

        return self._load()
