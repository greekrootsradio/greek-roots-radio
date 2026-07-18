import os
import datetime
import requests


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


    def check_core(self):

        try:

            response = requests.get(
                "http://127.0.0.1:5050",
                timeout=5
            )

            if response.status_code < 500:
                return "healthy"

            return "failed"


        except Exception:

            return "failed"



    def check_ollama(self):

        try:

            response = requests.get(
                "http://127.0.0.1:11434",
                timeout=5
            )

            if response.status_code < 500:
                return "healthy"

            return "failed"


        except Exception:

            return "failed"



    def check_memory(self):

        memory_file = os.path.expanduser(
            "~/cyprus/memory.json"
        )

        if os.path.exists(memory_file):

            return "healthy"

        return "failed"



    def check(self):

        self.write(
            "=== HEALTH CHECK START ==="
        )


        health = {

            "core": self.check_core(),

            "ollama": self.check_ollama(),

            "memory": self.check_memory()

        }


        self.write(
            f"Health result: {health}"
        )


        self.write(
            "=== HEALTH CHECK COMPLETE ==="
        )


        return health



if __name__ == "__main__":

    result = ZetaHealth().check()

    print(result)
