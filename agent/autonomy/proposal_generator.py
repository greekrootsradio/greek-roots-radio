from datetime import datetime


class ProposalGenerator:


    def __init__(self):

        self.name = "ZETA Proposal Generator"



    def generate(self, task):

        print(
            "[ZETA PROPOSAL] Analysing:",
            task
        )


        proposal = {


            "agent": self.name,


            "task": task,


            "analysis": {

                "type": "software development request",

                "goal": "prepare safe implementation proposal",

                "time": str(datetime.now())

            },


            "files": [

                "agent/memory/core.py",

                "agent/memory/manager.py",

                "agent/brain.py"

            ],


            "changes": [

                "create persistent memory storage",

                "add memory recall layer",

                "connect memory system to ZETA brain"

            ],


            "risk": "medium",


            "approval_required": True,


            "status": "proposal_ready",


            "time": str(datetime.now())

        }


        print(
            "[ZETA PROPOSAL] Ready"
        )


        return proposal
