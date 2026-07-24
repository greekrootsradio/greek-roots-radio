import os
import json
from datetime import datetime

from agent.memory.core import (
    get_memory,
    save_memory
)

from agent.memory.memory_guardian import MemoryGuardian


class MemoryManager:


    def __init__(self):

        self.memory = get_memory()
        self.guardian = MemoryGuardian()

        self.memory_file = "workspace/memory.json"



    def check_memory_health(self):

        return self.guardian.monitor(
            self.memory_file
        )



    def remember_fact(self, category, key, value):

        if category not in self.memory:
            self.memory[category] = {}

        self.memory[category][key] = value

        self.memory["last_updated"] = str(
            datetime.now()
        )

        save_memory(
            self.memory
        )

        return {
            "status": "stored",
            "category": category,
            "key": key,
            "value": value,
            "created": str(datetime.now())
        }



    def recall_fact(self, category, key):

        try:

            return {
                "status": "found",
                "value": self.memory[category][key],
                "created": str(datetime.now())
            }

        except KeyError:

            return {
                "status": "missing",
                "category": category,
                "key": key,
                "created": str(datetime.now())
            }



    def get_all_memory(self):

        return {
            "agent": "ZETA Memory Manager",
            "memory": self.memory,
            "created": str(datetime.now())
        }



    def rebuild_if_needed(self):

        health = self.check_memory_health()


        if health.get("integrity", {}).get("status") == "invalid":

            return {
                "status": "recovery_triggered",
                "health": health,
                "created": str(datetime.now())
            }


        return {
            "status": "memory healthy",
            "health": health,
            "created": str(datetime.now())
        }



    def export_memory(self):

        os.makedirs(
            "workspace",
            exist_ok=True
        )


        with open(
            "workspace/memory_export.json",
            "w"
        ) as f:

            json.dump(
                self.memory,
                f,
                indent=4
            )


        return {
            "status": "exported",
            "file": "workspace/memory_export.json",
            "created": str(datetime.now())
        }
