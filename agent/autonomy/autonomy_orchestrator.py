import os
import json
from datetime import datetime


from agent.autonomy.supervisor import SupervisorAgent
from agent.autonomy.improvement_planner import ImprovementPlanner
from agent.autonomy.proposal_queue import ProposalQueue
from agent.autonomy.approval_controller import ApprovalController
from agent.autonomy.repair_executor import RepairExecutor



class AutonomyOrchestrator:
    """
    ZETA Autonomy Orchestrator

    Complete controlled self-improvement pipeline:

    Failure
        |
        v
    Supervisor
        |
        v
    Diagnostics
        |
        v
    Improvement Planner
        |
        v
    Proposal Queue
        |
        v
    Approval Controller
        |
        v
    Repair Executor
        |
        v
    Validation
    """



    def __init__(self):

        self.agent = "ZETA Autonomy Orchestrator"


        self.supervisor = SupervisorAgent()

        self.planner = ImprovementPlanner()

        self.queue = ProposalQueue()

        self.approval = ApprovalController()

        self.executor = RepairExecutor()



        self.history_file = os.path.expanduser(
            "~/cyprus/workspace/autonomy_orchestrator.json"
        )


        self.history = []



    def process(self, failure):

        timestamp = str(datetime.now())


        result = {

            "agent": self.agent,

            "failure": failure,

            "created": timestamp

        }



        #
        # Stage 1
        # Supervisor investigation
        #

        supervisor_result = self.supervisor.run_check(
            failure
        )


        result["supervisor"] = supervisor_result




        #
        # Stage 2
        # Create improvement plan
        #

        plan = self.planner.create_plan(

            failure,

            "Improve ZETA reliability"

        )


        result["planner"] = plan





        #
        # Stage 3
        # Add proposal
        #

        proposal = self.queue.add_proposal(

            "improvement",

            plan["objective"]

        )


        result["proposal"] = proposal






        #
        # Stage 4
        # Approval gate
        #

        approval_result = self.approval.review(

            plan["objective"]

        )


        result["approval"] = approval_result





        if approval_result["decision"] != "approved":


            result["status"] = "blocked"


            self._save_history(result)


            return result






        #
        # Stage 5
        # Execute repair
        #

        execution = self.executor.execute(

            plan["objective"]

        )


        result["execution"] = execution





        #
        # Stage 6
        # Validation
        #

        validation = self.executor.validate(

            plan["objective"],

            "validation completed"

        )


        result["validation"] = validation





        result["status"] = "completed"



        self._save_history(result)



        return result





    def _save_history(self, data):


        self.history.append(data)



        directory = os.path.dirname(
            self.history_file
        )


        os.makedirs(

            directory,

            exist_ok=True

        )



        with open(

            self.history_file,

            "w"

        ) as f:


            json.dump(

                self.history,

                f,

                indent=4

            )
