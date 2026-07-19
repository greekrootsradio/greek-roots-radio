from datetime import datetime

from agent.memory import get_memory


def heartbeat():

    memory = get_memory()

    report = {
        "time": datetime.now().isoformat(),
        "user": memory["user_profile"],
        "projects": memory["projects"],
        "goals": memory["goals"],
        "status": "ZETA autonomy heartbeat active"
    }

    return report


if __name__ == "__main__":

    print(heartbeat())
