from datetime import datetime

from agent.memory import get_memory, update_memory


def record_learning(action_results):

    memory = get_memory()

    knowledge = memory.get("knowledge", {})

    knowledge["last_autonomy_cycle"] = "completed"

    knowledge["actions_completed"] = len(action_results)

    if action_results:
        knowledge["last_action"] = action_results[-1]["action"]
    else:
        knowledge["last_action"] = "none"

    knowledge["last_update"] = datetime.now().isoformat()


    update_memory(
        "knowledge",
        knowledge
    )


    return knowledge



def main():

    print("ZETA LEARNING SYSTEM")


    actions = [
        {
            "action": "Create development checklist",
            "result": "completed"
        },
        {
            "action": "Review project",
            "result": "completed"
        }
    ]


    result = record_learning(actions)


    print(result)



if __name__ == "__main__":
    main()
