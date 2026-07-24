import subprocess
import os
from datetime import datetime


class TesterAgent:


    def __init__(self):

        self.name = "ZETA Tester Agent"

        self.project = os.path.expanduser(
            "~/cyprus"
        )


    def run_tests(self):

        try:

            result = subprocess.run(
                [
                    "python3",
                    "-m",
                    "pytest"
                ],
                cwd=self.project,
                capture_output=True,
                text=True
            )


            return {

                "agent":
                    self.name,

                "status":
                    "passed"
                    if result.returncode == 0
                    else "failed",

                "output":
                    result.stdout[-1000:],

                "errors":
                    result.stderr[-1000:],

                "time":
                    str(datetime.now())

            }


        except Exception as e:

            return {

                "agent":
                    self.name,

                "status":
                    "error",

                "message":
                    str(e),

                "time":
                    str(datetime.now())

            }
