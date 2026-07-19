from agent.memory import get_memory, save_memory


def add_task(task):

    memory = get_memory()

    if "tasks" not in memory:
        memory["tasks"] = []

    memory["tasks"].append({
        "task": task,
        "status": "pending"
    })

    save_memory(memory)



def get_tasks():

    memory = get_memory()

    return memory.get("tasks", [])



if __name__ == "__main__":

    add_task(
        "Build ZETA autonomous planning system"
    )

    add_task(
        "Develop Greek Roots Radio AI workflow"
    )

    print("ZETA TASKS")

    for task in get_tasks():
        print(task)
