import os
from datetime import datetime


class HealthMonitor:

    def __init__(self):

        self.name = "ZETA Health Monitor"


    def check_component(
        self,
        component,
        status
    ):

        return {

            "component":
                component,

            "status":
                status

        }



    def system_report(self):

        checks = [

            self.check_component(
                "Autonomy Controller",
                "OK"
            ),

            self.check_component(
                "Diagnostics",
                "OK"
            ),

            self.check_component(
                "Failure Memory",
                "OK"
            ),

            self.check_component(
                "Repair History",
                "OK"
            ),

            self.check_component(
                "Tester",
                "WARNING"
            ),

            self.check_component(
                "Git Manager",
                "OK"
            )

        ]


        return {

            "agent":
                self.name,

            "checks":
                checks,

            "created":
                str(datetime.now())

        }
