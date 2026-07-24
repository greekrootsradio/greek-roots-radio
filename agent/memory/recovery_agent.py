import os
import json
from datetime import datetime


class MemoryRecoveryAgent:

    def __init__(self):

        self.workspace = os.path.expanduser(
            "~/cyprus/workspace"
        )

        self.history_file = os.path.join(
            self.workspace,
            "memory_recovery_history.json"
        )

        os.makedirs(
            self.workspace,
            exist_ok=True
        )


    def _load_history(self):

        if not os.path.exists(self.history_file):
            return []

        try:
            with open(
                self.history_file,
                "r"
            ) as f:
                return json.load(f)

        except Exception:
            return []


    def _save_history(self, history):

        with open(
            self.history_file,
            "w"
        ) as f:
            json.dump(
                history,
                f,
                indent=4
            )


    def check_memory(self, memory_file):

        result = {
            "agent": "ZETA Memory Recovery Agent",
            "file": memory_file,
            "created": str(datetime.now())
        }


        if not os.path.exists(memory_file):

            result.update(
                {
                    "status": "missing",
                    "action": "request rebuild"
                }
            )

        else:

            try:

                with open(
                    memory_file,
                    "r"
                ) as f:

                    json.load(f)


                result.update(
                    {
                        "status": "healthy",
                        "action": "no recovery required"
                    }
                )


            except Exception as e:

                result.update(
                    {
                        "status": "corrupted",
                        "action": "prepare recovery",
                        "error": str(e)
                    }
                )


        history = self._load_history()

        history.append(result)

        self._save_history(history)

        return result



    def rebuild_memory(self, memory_file):

        result = {
            "agent": "ZETA Memory Recovery Agent",
            "task": "memory rebuild",
            "file": memory_file,
            "status": "rebuilt",
            "created": str(datetime.now())
        }


        history = self._load_history()

        history.append(result)

        self._save_history(history)


        return result



    def history(self):

        return self._load_history()
