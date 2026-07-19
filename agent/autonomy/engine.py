from datetime import datetime

from agent.autonomy.status import get_status
from agent.autonomy.planner import generate_plan


def run_engine():

    print("\nZETA AUTONOMY ENGINE\n")


    print("SYSTEM INSPECTION:")

    status = get_status()

    print({
        "time": status["time"],
        "user": status["user"],
        "projects": status["projects"],
        "goals": status["goals"],
        "tasks": status["tasks"]
    })


    print("\nTHOUGHT PROCESS:")

    plans = generate_plan()

    for plan in plans:

        print({
            "type": plan["type"],
            "action": plan["next_action"],
            "created": datetime.now().isoformat()
        })


if __name__ == "__main__":
    run_engine()
