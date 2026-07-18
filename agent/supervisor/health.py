import os
import json
import datetime
import urllib.request


class ZetaHealth:

    def __init__(self):

        self.log = os.path.expanduser(
            "~/cyprus/workspace/logs/zeta_health.log"
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


    def check(self):

        self.write("=== ZETA HEALTH CHECK ===")


        # memory
        memory = os.path.expanduser(
            "~/cyprus/memory.json"
        )

        if os.path.exists(memory):
            self.write("Memory: OK")
        else:
            self.write("Memory: ERROR")


        # Flask
        try:
            urllib.request.urlopen(
                "http://127.0.0.1:5050",
                timeout=3
            )
            self.write("Core API: OK")

        except Exception as e:
            self.write(
                f"Core API: ERROR {e}"
            )


        self.write("Health check complete")


if __name__ == "__main__":

    ZetaHealth().check()
