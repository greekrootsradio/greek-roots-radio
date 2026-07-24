import os
from datetime import datetime


class EditorAgent:


    def __init__(self):

        self.name = "ZETA Editor Agent"

        self.project = os.path.expanduser(
            "~/cyprus"
        )


    def read_file(self, path):

        full_path = os.path.join(
            self.project,
            path
        )

        if not os.path.exists(full_path):

            return {
                "status": "error",
                "message": "File does not exist"
            }


        with open(
            full_path,
            "r"
        ) as f:

            content = f.read()


        return {
            "status": "success",
            "file": path,
            "content": content
        }


    def propose_change(
        self,
        path,
        description
    ):

        return {

            "agent":
                self.name,

            "file":
                path,

            "proposal":
                description,

            "status":
                "awaiting approval",

            "created":
                str(datetime.now())

        }
