import os
from datetime import datetime

from agent.decision.decision_engine import DecisionEngine
from agent.proposals.proposal_manager import ProposalManager


class AutonomyOrchestrator:

    def __init__(self):

        self.name = "ZETA Autonomy Orchestrator"

        self.decision = DecisionEngine()

        self.proposals = ProposalManager()


    def analyse(
        self,
        situation,
        options
    ):

        print()
        print("==============================")
        print("ZETA AUTONOMY ORCHESTRATOR")
        print("==============================")

        decision = self.decision.evaluate(
            situation,
            options
        )


        proposal = self.proposals.create(
            title=decision["recommendation"],
            reason=situation,
            action=decision["recommendation"]
        )


        print("✓ Decision created")
        print("✓ Proposal created")


        return {

            "agent":
                self.name,

            "created":
                str(datetime.now()),

            "decision":
                decision,

            "proposal":
                proposal

        }
