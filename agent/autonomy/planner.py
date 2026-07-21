from agent.memory import get_memory
from datetime import datetime


class PlannerAgent:


    def __init__(self):

        self.name = "ZETA Planner Agent"



    def generate_plan(self):

        memory = get_memory()


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

                "created": str(datetime.now())

            }


        if projects:

            project = list(projects.keys())[0]

            return {

                "module": "project_manager",

                "purpose": project,

                "created": str(datetime.now())

            }


        return {

            "module": "system_improvement",

            "purpose": "Improve ZETA autonomous maintenance system",

            "created": str(datetime.now())

        }



def generate_plan():

    planner = PlannerAgent()

    return planner.generate_plan()



if __name__ == "__main__":

    planner = PlannerAgent()

    print(
        planner.generate_plan()
    )
