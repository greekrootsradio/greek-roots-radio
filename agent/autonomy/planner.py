from agent.memory import get_memory
from datetime import datetime


def generate_plan():

    memory = get_memory()

    plans = []

    goals = memory.get("goals", [])

    for goal in goals:

        plans.append({
            "type": "goal",
            "goal": goal,
            "next_action": "Analyse requirements and create task list"
        })


    projects = memory.get("projects", {})

    for project in projects:

        plans.append({
            "type": "project",
            "project": project,
            "next_action": "Review project status and identify improvements"
        })


    return plans


def main():

    print("ZETA PLANNER")

    plans = generate_plan()

    for plan in plans:
        print(plan)


if __name__ == "__main__":
    main()
