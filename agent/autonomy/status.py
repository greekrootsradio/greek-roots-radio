from datetime import datetime
from agent.memory import get_memory


def get_status():

    memory = get_memory()

    return {
        "time": datetime.now().isoformat(),
        "user": memory.get("user_profile", {}),
        "projects": memory.get("projects", {}),
        "goals": memory.get("goals", []),
        "tasks": memory.get("tasks", []),
        "system": "ZETA autonomy heartbeat active"
    }


def main():

    status = get_status()

    print("\nZETA STATUS REPORT\n")

    print("Time:")
    print(status["time"])

    print("\nUser:")
    print(status["user"])

    print("\nProjects:")
    print(status["projects"])

    print("\nGoals:")
    print(status["goals"])

    print("\nTasks:")
    print(status["tasks"])

    print("\nSystem:")
    print(status["system"])


if __name__ == "__main__":
    main()
