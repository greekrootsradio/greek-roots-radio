import json
import os
from datetime import datetime


class ProposalManager:

    def __init__(self):

        self.name = "ZETA Proposal Manager"

        self.file = os.path.expanduser(
            "~/cyprus/workspace/proposals.json"
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


    def create(
        self,
        title,
        reason,
        action
    ):

        proposal = {

            "agent":
                self.name,

            "title":
                title,

            "reason":
                reason,

            "proposed_action":
                action,

            "status":
                "awaiting approval",

            "created":
                str(datetime.now())

        }


        history = self._load()

        history.append(proposal)

        self._save(history)

        return proposal


    def history(self):

        return self._load()
