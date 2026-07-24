from datetime import datetime


class RepairAgent:


    def __init__(self):

        self.name = "ZETA Repair Agent"


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
                "Investigate failing component before proposing change",

            "status":
                "proposal required",

            "created":
                str(datetime.now())

        }


    def propose_fix(
        self,
        file,
        reason
    ):

        return {

            "agent":
                self.name,

            "file":
                file,

            "reason":
                reason,

            "action":
                "prepare repair proposal",

            "status":
                "awaiting approval",

            "created":
                str(datetime.now())

        }
