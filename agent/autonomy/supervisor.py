from agent.autonomy.logger import ZetaLogger
from agent.autonomy.self_inspector import SelfInspector
from agent.autonomy.development_cycle import DevelopmentCycle
from agent.autonomy.experience_engine import ExperienceEngine
from agent.autonomy.worker import ZetaWorker
from agent.autonomy.goal_orchestrator import GoalOrchestrator
from agent.autonomy.goal_evaluator import GoalEvaluator


class ZetaSupervisor:


    def __init__(self):

        self.logger = ZetaLogger()

        self.inspector = SelfInspector()

        self.development = DevelopmentCycle()

        self.experience = ExperienceEngine()

        self.worker = ZetaWorker()

        self.goal_orchestrator = GoalOrchestrator()

        self.evaluator = GoalEvaluator()



    def run_cycle(self):

        print(
            "[ZETA SUPERVISOR] Starting autonomous cycle"
        )


        self.logger.write(
            "Supervisor autonomous cycle started"
        )


        print(
            "[ZETA SUPERVISOR] Inspecting system"
        )


        inspection = self.inspector.inspect()


        print(
            "[ZETA INSPECTOR]",
        )

        print(
            inspection
        )



        print(
            "[ZETA SUPERVISOR] Selecting next goal"
        )


        goal = self.goal_orchestrator.choose_goal()


        action = self.goal_orchestrator.create_action(
            goal
        )


        print(
            "[ZETA SUPERVISOR] Action:",
            action
        )



        print(
            "[ZETA SUPERVISOR] Running worker"
        )


        result = self.worker.run()



        print(
            "[ZETA SUPERVISOR] Evaluating result"
        )


        evaluation = self.evaluator.evaluate(
            action,
            result
        )



        print(
            "[ZETA SUPERVISOR] Running development maintenance"
        )


        development_result = self.development.run()



        experience_result = self.experience.record(

            {

                "inspection": inspection,

                "goal": goal,

                "action": action,

                "worker": result,

                "evaluation": evaluation,

                "development": development_result

            }

        )



        print(
            "[ZETA SUPERVISOR] Cycle complete"
        )


        return {


            "inspection": inspection,

            "goal": goal,

            "action": action,

            "worker": result,

            "evaluation": evaluation,

            "development": development_result,

            "experience": experience_result

        }



if __name__ == "__main__":


    supervisor = ZetaSupervisor()


    result = supervisor.run_cycle()


    print()

    print(
        "[ZETA SUPERVISOR RESULT]"
    )

    print(
        result
    )
