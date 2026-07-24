import os
import json
from datetime import datetime


class MemoryConsolidator:

    def __init__(self):

        self.history_file = os.path.expanduser(
            "~/cyprus/workspace/memory_consolidation_history.json"
        )

        os.makedirs(
            os.path.dirname(self.history_file),
            exist_ok=True
        )


    def _load_history(self):

        if not os.path.exists(self.history_file):
            return []

        with open(
            self.history_file,
            "r"
        ) as f:
            return json.load(f)



    def _save_history(self, data):

        with open(
            self.history_file,
            "w"
        ) as f:
            json.dump(
                data,
                f,
                indent=4
            )



    def analyse(self, memory_file):

        now = str(datetime.now())

        if not os.path.exists(memory_file):

            result = {
                "agent": "ZETA Memory Consolidator",
                "file": memory_file,
                "created": now,
                "status": "failed",
                "reason": "memory file missing"
            }

            self._record(result)

            return result


        with open(
            memory_file,
            "r"
        ) as f:

            memory = json.load(f)


        categories = list(
            memory.keys()
        )


        result = {

            "agent":
                "ZETA Memory Consolidator",

            "file":
                memory_file,

            "created":
                now,

            "analysis": {

                "categories":
                    categories,

                "category_count":
                    len(categories),

                "status":
                    "healthy"

            },

            "recommendation":
                "review memories and optimise storage"

        }


        self._record(result)

        return result



    def consolidate(self, memory_file):

        now = str(datetime.now())


        if not os.path.exists(memory_file):

            return {

                "agent":
                    "ZETA Memory Consolidator",

                "status":
                    "failed",

                "reason":
                    "memory file missing"

            }


        with open(
            memory_file,
            "r"
        ) as f:

            memory = json.load(f)



        cleaned = {}


        for key, value in memory.items():

            cleaned[key] = value



        with open(
            memory_file,
            "w"
        ) as f:

            json.dump(
                cleaned,
                f,
                indent=4
            )


        result = {

            "agent":
                "ZETA Memory Consolidator",

            "task":
                "memory consolidation",

            "file":
                memory_file,

            "status":
                "completed",

            "created":
                now

        }


        self._record(result)


        return result



    def _record(self, item):

        history = self._load_history()

        history.append(item)

        self._save_history(history)



    def history(self):

        return self._load_history()
