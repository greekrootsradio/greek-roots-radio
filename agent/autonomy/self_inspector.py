import os
from datetime import datetime


class SelfInspector:

    def __init__(self):

        self.root = os.path.expanduser("~/cyprus")


    def inspect(self):

        modules = []

        autonomy = os.path.join(
            self.root,
            "agent/autonomy"
        )

        for file in os.listdir(autonomy):

            if file.endswith(".py"):
                modules.append(file)


        report = {
            "time": str(datetime.now()),
            "modules": modules,
            "count": len(modules)
        }


        print("[ZETA INSPECTOR]")
        print(report)

        return report
