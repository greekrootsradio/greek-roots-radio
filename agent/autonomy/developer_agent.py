import os
from datetime import datetime


class DeveloperAgent:


    def __init__(self):

        self.name = "ZETA Developer Agent"


        self.project = os.path.expanduser(
            "~/cyprus"
        )



    def inspect_project(self):

        files = []


        for root, dirs, filenames in os.walk(
            self.project
        ):

            for filename in filenames:

                if filename.endswith(".py"):

                    path = os.path.join(
                        root,
                        filename
                    )

                    files.append(
                        path.replace(
                            self.project,
                            ""
                        )
                    )


        return files[:50]



    def analyse_task(self, task):

        analysis = {

            "task": task,

            "type":
                "software development request",

            "goal":
                "understand required changes before editing",

            "time":
                str(datetime.now())

        }


        return analysis



    def create_plan(
        self,
        task,
        files
    ):

        plan = {

            "task": task,

            "possible_files": files,

            "steps": [

                "inspect existing code",

                "design change",

                "implement safely",

                "run tests",

                "report result"

            ]

        }


        return plan



    def build(
        self,
        task
    ):

        print(
            "[ZETA DEVELOPER] Analysing:",
            task
        )


        files = self.inspect_project()


        analysis = self.analyse_task(
            task
        )


        plan = self.create_plan(
            task,
            files
        )


        result = {

            "agent":
                self.name,

            "task":
                task,

            "action":
                "development planning",

            "analysis":
                analysis,

            "plan":
                plan,

            "status":
                "planned",

            "time":
                str(datetime.now())

        }


        print(
            "[ZETA DEVELOPER] Plan created"
        )


        return result
