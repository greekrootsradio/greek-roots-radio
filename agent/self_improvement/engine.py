import os
from datetime import datetime

from agent.self_improvement.coder import ZetaCoder
from agent.self_improvement.manager import SelfImprovementManager


class SelfImprovementEngine:

    def __init__(self):
        self.coder = ZetaCoder()
        self.manager = SelfImprovementManager()


    def improve(self, target_file, idea):

        print("ZETA SELF IMPROVEMENT START")

        proposal = self.coder.create_proposal(
            target_file.replace("/", "_"),
            idea
        )

        print("Proposal created:")
        print(proposal)

        approval = self.manager.approve_change(
            target_file
        )

        print("Backup created:")
        print(approval)

        return {
            "proposal": proposal,
            "backup": approval
        }
