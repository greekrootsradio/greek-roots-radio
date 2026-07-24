from datetime import datetime


class ProposalQueue:

    def __init__(self):

        self.name = "ZETA Proposal Queue"
        self.queue = []


    def add_proposal(
        self,
        proposal_type,
        description,
        status="awaiting approval"
    ):

        proposal = {

            "type":
                proposal_type,

            "description":
                description,

            "status":
                status,

            "created":
                str(datetime.now())

        }

        self.queue.append(proposal)

        return proposal


    def get_pending(self):

        return [
            p for p in self.queue
            if p["status"] == "awaiting approval"
        ]


    def approve(
        self,
        index
    ):

        if index < len(self.queue):

            self.queue[index]["status"] = "approved"

            return self.queue[index]

        return {
            "error": "proposal not found"
        }
