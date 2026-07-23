from datetime import datetime


class ApprovalGate:

    def __init__(self):

        self.name = "ZETA Approval Gate"


    def review(self, proposal):

        print("[ZETA APPROVAL] Reviewing proposal")

        risk = proposal.get(
            "risk",
            "unknown"
        )

        result = {

            "gate": self.name,

            "proposal": proposal.get(
                "task",
                "unknown"
            ),

            "risk": risk,

            "approved": False,

            "reason": "awaiting human approval",

            "time": str(datetime.now())

        }


        print(
            "[ZETA APPROVAL] Decision:",
            result["approved"]
        )

        return result
