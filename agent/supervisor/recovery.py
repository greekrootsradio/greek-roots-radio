import os
import subprocess
import datetime
import time


class SupervisorRecovery:


    def __init__(self):

        self.log = os.path.expanduser(
            "~/cyprus/workspace/logs/zeta_recovery.log"
        )

        os.makedirs(
            os.path.dirname(self.log),
            exist_ok=True
        )


    def write(self, message):

        with open(self.log, "a") as f:
            f.write(
                f"{datetime.datetime.now()} {message}\n"
            )


    def restart_core(self):

        self.write(
            "CORE recovery started"
        )

        try:

            subprocess.run(
                [
                    "pkill",
                    "-f",
                    "main.py"
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )


            time.sleep(3)


            subprocess.Popen(
                [
                    "python3",
                    "main.py"
                ],
                cwd=os.path.expanduser(
                    "~/cyprus"
                )
            )


            self.write(
                "CORE restarted successfully"
            )

            return "core_recovered"


        except Exception as e:

            self.write(
                f"CORE recovery failed: {e}"
            )

            return "core_recovery_failed"



    def restart_ollama(self):

        self.write(
            "OLLAMA recovery started"
        )

        try:

            subprocess.run(
                [
                    "pkill",
                    "ollama"
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )


            time.sleep(3)


            subprocess.Popen(
                [
                    "ollama",
                    "serve"
                ]
            )


            self.write(
                "OLLAMA restarted successfully"
            )

            return "ollama_recovered"


        except Exception as e:

            self.write(
                f"OLLAMA recovery failed: {e}"
            )

            return "ollama_recovery_failed"



    def repair_memory(self):

        self.write(
            "MEMORY recovery started"
        )


        memory_file = os.path.expanduser(
            "~/cyprus/memory.json"
        )


        if os.path.exists(memory_file):

            self.write(
                "Memory file exists - no repair required"
            )

            return "memory_ok"



        try:

            with open(memory_file, "w") as f:

                f.write(
                    "{}"
                )


            self.write(
                "Memory file recreated"
            )

            return "memory_repaired"



        except Exception as e:

            self.write(
                f"Memory repair failed: {e}"
            )

            return "memory_repair_failed"



if __name__ == "__main__":

    recovery = SupervisorRecovery()

    print(
        recovery.repair_memory()
    )
