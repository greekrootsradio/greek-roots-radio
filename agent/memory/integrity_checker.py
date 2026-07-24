import os
import json
from datetime import datetime


class MemoryIntegrityChecker:

    def __init__(self):

        self.workspace = os.path.expanduser(
            "~/cyprus/workspace"
        )

        self.history_file = os.path.join(
            self.workspace,
            "memory_integrity_history.json"
        )

        os.makedirs(
            self.workspace,
            exist_ok=True
        )


    def _load_history(self):

        if not os.path.exists(
            self.history_file
        ):
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


    def check(self, memory_file):

        report = {
            "agent": "ZETA Memory Integrity Checker",
            "file": memory_file,
            "created": str(datetime.now()),
            "checks": []
        }


        if not os.path.exists(memory_file):

            report["checks"].append(
                {
                    "test": "file_exists",
                    "status": "failed",
                    "reason": "memory file missing"
                }
            )

            report["status"] = "invalid"


        else:

            report["checks"].append(
                {
                    "test": "file_exists",
                    "status": "passed"
                }
            )


            try:

                with open(
                    memory_file,
                    "r"
                ) as f:

                    data = json.load(f)


                report["checks"].append(
                    {
                        "test": "json_format",
                        "status": "passed"
                    }
                )


                if isinstance(data, dict):

                    report["checks"].append(
                        {
                            "test": "memory_structure",
                            "status": "passed"
                        }
                    )

                    report["status"] = "healthy"


                else:

                    report["checks"].append(
                        {
                            "test": "memory_structure",
                            "status": "failed",
                            "reason": "unexpected format"
                        }
                    )

                    report["status"] = "invalid"



            except Exception as e:

                report["checks"].append(
                    {
                        "test": "json_format",
                        "status": "failed",
                        "error": str(e)
                    }
                )

                report["status"] = "corrupted"



        history = self._load_history()

        history.append(
            report
        )

        self._save_history(
            history
        )


        return report



    def history(self):

        return self._load_history()
