import json
import os
from datetime import datetime


class MissionManager:

    def __init__(self):

        self.file = os.path.expanduser(
            "~/cyprus/workspace/projects/radio_missions.json"
        )

        self.default_missions = [
            "Create Station Introduction",
            "Create Facebook Post",
            "Create Instagram Caption",
            "Create Daily Playlist",
            "Create DJ Script",
            "Create Website Homepage",
            "Create Sponsor Proposal",
            "Create Listener Competition",
            "Create Community News",
            "Create Marketing Idea"
        ]

        self._ensure_file()

    def _ensure_file(self):

        if not os.path.exists(self.file):

            os.makedirs(
                os.path.dirname(self.file),
                exist_ok=True
            )

            data = {
                "current_index": 0,
                "missions": self.default_missions,
                "created": str(datetime.now())
            }

            with open(self.file, "w") as f:
                json.dump(data, f, indent=4)

    def next_mission(self):

        with open(self.file, "r") as f:
            data = json.load(f)

        index = data["current_index"]

        mission = data["missions"][index]

        index += 1

        if index >= len(data["missions"]):
            index = 0

        data["current_index"] = index

        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

        return mission
