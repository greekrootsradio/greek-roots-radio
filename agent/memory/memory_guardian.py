import os
from datetime import datetime

from agent.memory.integrity_checker import MemoryIntegrityChecker
from agent.memory.recovery_agent import MemoryRecoveryAgent


class MemoryGuardian:

    def __init__(self):

        self.name = "ZETA Memory Guardian"

        self.memory_file = os.path.expanduser(
            "~/cyprus/data/memory.json"
        )

        self.integrity = MemoryIntegrityChecker()

        self.recovery = MemoryRecoveryAgent()


    def monitor(self):

        result = {

            "agent": self.name,

            "memory_file": self.memory_file,

            "created": str(datetime.now())

        }


        check = self.integrity.check(
            self.memory_file
        )


        result["integrity"] = check


        if check["status"] == "healthy":

            result["action"] = "memory healthy"

        else:

            result["action"] = "memory recovery requested"

            result["recovery"] = self.recovery.rebuild_memory(
                self.memory_file
            )


        return result


    def history(self):

        return []
