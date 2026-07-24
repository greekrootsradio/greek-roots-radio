import os
from datetime import datetime


class DiagnosticsAgent:

    def __init__(self):

        self.name = "ZETA Diagnostics Agent"

        self.log_file = os.path.expanduser(
            "~/cyprus/workspace/logs/zeta_diagnostics.log"
        )


    def record_failure(
        self,
        failure,
        component,
        severity="medium"
    ):

        report = {

            "agent": self.name,

            "failure":
                failure,

            "component":
                component,

            "severity":
                severity,

            "status":
                "recorded",

            "created":
                str(datetime.now())

        }


        os.makedirs(
            os.path.dirname(self.log_file),
            exist_ok=True
        )


        with open(
            self.log_file,
            "a"
        ) as f:

            f.write(
                str(report)
                + "\n"
            )


        return report



    def analyse_failure(
        self,
        failure
    ):

        return {

            "agent":
                self.name,

            "failure":
                failure,

            "analysis":
                "Failure captured for investigation",

            "next":
                "send to repair planner",

            "created":
                str(datetime.now())

        }
