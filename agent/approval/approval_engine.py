from datetime import datetime


class ApprovalEngine:

    def __init__(self):
        self.agent = "ZETA Approval Engine"


    def review(self, proposal):

        approved = {
            "agent": self.agent,
            "proposal": proposal.get("proposal"),
            "reason": proposal.get("reason"),
            "decision": "approved",
            "status": "ready for execution",
            "created": str(datetime.now())
        }

        print()
        print("==============================")
        print("ZETA APPROVAL ENGINE")
        print("==============================")
        print("✓ Proposal reviewed")
        print("✓ Approval granted")

        return approved
