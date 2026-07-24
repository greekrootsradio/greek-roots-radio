import subprocess
from datetime import datetime


class GitManagerAgent:


    def __init__(self):

        self.name = "ZETA Git Manager Agent"


    def status(self):

        result = subprocess.run(
            [
                "git",
                "status",
                "--short"
            ],
            capture_output=True,
            text=True
        )

        return result.stdout.strip()


    def create_proposal(
        self,
        task
    ):

        changes = self.status()


        return {

            "agent":
                self.name,

            "task":
                task,

            "changes":
                changes,

            "proposal":
                "create git checkpoint",

            "status":
                "awaiting approval",

            "created":
                str(datetime.now())

        }
