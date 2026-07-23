import json
import os
from datetime import datetime


class MemoryStorage:

    def __init__(self):

        self.file = os.path.expanduser(
            "~/cyprus/data/zeta_memory.json"
        )

        os.makedirs(
            os.path.dirname(self.file),
            exist_ok=True
        )

        if not os.path.exists(self.file):
            self._create()


    def _create(self):

        with open(self.file, "w") as f:
            json.dump(
                [],
                f,
                indent=4
            )


    def save(self, memory):

        memory["created"] = str(
            datetime.now()
        )

        data = self.load()

        data.append(memory)

        with open(self.file, "w") as f:
            json.dump(
                data,
                f,
                indent=4
            )

        return memory


    def load(self):

        with open(self.file, "r") as f:
            return json.load(f)
