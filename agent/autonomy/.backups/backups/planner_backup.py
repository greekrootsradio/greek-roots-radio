from datetime import datetime

from agent.memory import get_memory


class PlannerAgent:


    def __init__(self):

        self.name = "ZETA Planner Agent"



    def generate_plan(self, decision=None):

        memory = get_memory()


        if decision:

            chosen_goal = decision.get(
                "decision",
                {}
            ).get(
                "chosen_goal"
            )


            if chosen_goal:

                return {

                    "module": chosen_goal,

                    "purpose": (
                        "Execute selected autonomy goal"
                    ),

                    "created": str(
                        datetime.now()
                    )

                }



        goals = memory.get(
            "goals",
            []
        )


        projects = memory.get(
            "projects",
            {}
        )


        if goals:

            return {

                "module": "goal_manager",

                "purpose": goals[0],

                "created": str(
                    datetime.now()
                )

            }


        if projects:

            project = list(
                projects.keys()
            )[0]


            return {

                "module": "project_manager",

                "purpose": project,

                "created": str(
                    datetime.now()
                )

            }


        return {

            "module": "system_improvement",

            "purpose": (
                "Improve ZETA autonomous maintenance system"
            ),

            "created": str(
                datetime.now()
            )

        }



def generate_plan(decision=None):

    planner = PlannerAgent()

    return planner.generate_plan(
        decision
    )



if __name__ == "__main__":

    planner = PlannerAgent()

    print(
        planner.generate_plan()
    )
