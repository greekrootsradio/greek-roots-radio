import os
from datetime import datetime

from agent.memory.integrity_checker import MemoryIntegrityChecker
from agent.memory.recovery_agent import MemoryRecoveryAgent


class MemoryGuardian:

    def __init__(self):

        self.agent = "ZETA Memory Guardian"

        self.history_file = os.path.expanduser(
            "~/cyprus/workspace/memory_guardian_history.json"
        )

        self.integrity = MemoryIntegrityChecker()
        self.recovery = MemoryRecoveryAgent()

        os.makedirs(
            os.path.dirname(self.history_file),
            exist_ok=True
        )


    def _record(self, entry):

        import json

        history = []

        if os.path.exists(self.history_file):

            with open(
                self.history_file,
                "r"
            ) as f:
                try:
                    history = json.load(f)
                except:
                    history = []


        history.append(entry)


        with open(
            self.history_file,
            "w"
        ) as f:
            json.dump(
                history,
                f,
                indent=4
            )


    def monitor(self, memory_file):

        check = self.integrity.check(
            memory_file
        )


        result = {

            "agent": self.agent,

            "memory_file": memory_file,

            "created": str(
                datetime.now()
            ),

            "integrity": check,

            "action": "none"

        }


        if check["status"] == "invalid":

            result["action"] = (
                "memory recovery requested"
            )

            result["recovery"] = (
                self.recovery.rebuild_memory(
                    memory_file
                )
            )

        else:

            result["action"] = (
                "memory healthy"
            )


        self._record(result)


        return result



    def history(self):

        import json


        if not os.path.exists(
            self.history_file
        ):
            return []


        with open(
            self.history_file,
            "r"
        ) as f:

            return json.load(f)
