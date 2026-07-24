import os
import json
from datetime import datetime


class TestAgent:

    def __init__(self):

        self.file = os.path.expanduser(
            "~/cyprus/workspace/test_results.json"
        )

        os.makedirs(
            os.path.dirname(self.file),
            exist_ok=True
        )


    def _save(self, record):

        data = []

        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                data = json.load(f)

        data.append(record)

        with open(self.file, "w") as f:
            json.dump(
                data,
                f,
                indent=4
            )


    def run_test(self, component, result):

        record = {
            "agent": "ZETA Test Agent",
            "component": component,
            "result": result,
            "status": "passed"
                if result
                else "failed",
            "created": str(datetime.now())
        }

        self._save(record)

        return record


    def history(self):

        if not os.path.exists(self.file):
            return []

        with open(self.file, "r") as f:
            return json.load(f)
