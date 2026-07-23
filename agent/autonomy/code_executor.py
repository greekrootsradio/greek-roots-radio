import os
from datetime import datetime


class CodeExecutor:


    def __init__(self):

        self.name = "ZETA Code Executor"



    def inspect_file(self, path):

        full_path = os.path.expanduser(
            "~/cyprus/" + path
        )


        if not os.path.exists(full_path):

            return {

                "exists": False,

                "path": path,

                "checked": str(datetime.now())

            }


        return {

            "exists": True,

            "path": path,

            "size": os.path.getsize(full_path),

            "checked": str(datetime.now())

        }



    def inspect_directory(self, path):

        full_path = os.path.expanduser(
            "~/cyprus/" + path
        )


        if not os.path.exists(full_path):

            return {

                "exists": False,

                "path": path,

                "checked": str(datetime.now())

            }


        files = []


        for root, directories, filenames in os.walk(full_path):

            for filename in filenames:

                files.append(
                    os.path.join(
                        root,
                        filename
                    )
                )


        return {

            "exists": True,

            "path": path,

            "files_found": len(files),

            "files": files[:50],

            "checked": str(datetime.now())

        }



    def propose_change(self, task):

        return {

            "executor": self.name,

            "task": task,

            "action": "proposal only",

            "safety": "no files modified",

            "approval_required": True,

            "time": str(datetime.now())

        }



    def create_plan(self, task, files=None):

        return {

            "executor": self.name,

            "task": task,

            "files": files or [],

            "plan": [

                "inspect existing code",

                "identify required changes",

                "prepare modification proposal",

                "await approval"

            ],

            "status": "planned",

            "time": str(datetime.now())

        }
