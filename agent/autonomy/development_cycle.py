from agent.autonomy.self_monitor import SelfMonitor
from agent.autonomy.planner import PlannerAgent
from agent.autonomy.coder import CodeWriter
from agent.autonomy.tester import TesterAgent
from agent.autonomy.reviewer import ReviewerAgent


class DevelopmentCycle:

    def __init__(self):

        self.monitor = SelfMonitor()
        self.planner = PlannerAgent()
        self.coder = CodeWriter()
        self.tester = TesterAgent()
        self.reviewer = ReviewerAgent()


    def run(self):

        print("[Development] Running health check...")

        health = self.monitor.check()

        if not health["memory"]:
            print("[Development] Memory unavailable.")
            return

        if not health["workspace"]:
            print("[Development] Workspace unavailable.")
            return


        print("[Development] Health OK")


        plan = self.planner.generate_plan()


        if plan is None:

            print("[Development] Nothing to build.")
            return


        self.coder.create_module(
            plan["module"],
            plan["purpose"]
        )


        print(
            f"[Development] Proposal created: {plan['module']}"
        )


        self.tester.test_all()


        self.reviewer.review()
