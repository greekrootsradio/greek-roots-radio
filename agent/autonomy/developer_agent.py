import os
from datetime import datetime

from agent.autonomy.executor import Executor


class DeveloperAgent:

    def __init__(self):

        self.name = "ZETA Developer Agent"

        self.project = os.path.expanduser(
            "~/cyprus"
        )

        self.executor = Executor()

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

        print(
            "[ZETA DEVELOPER] Plan created"
        )

        execution = self.executor.execute(
            plan
        )

        result = {

            "agent":
                self.name,

            "task":
                task,

            "action":
                "development execution",

            "analysis":
                analysis,

            "plan":
                plan,

            "execution":
                execution,

            "status":
                execution["status"],

            "time":
                str(datetime.now())

        }

        return result
