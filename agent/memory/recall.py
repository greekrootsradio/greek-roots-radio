from agent.memory.core import get_memory


def recall_memory(message):

    memory = get_memory()

    results = {}

    text = message.lower()


    # projects

    for project in memory.get("projects", {}):

        if project.lower() in text or "project" in text:

            results["projects"] = memory["projects"]


    # preferences

    for key,value in memory.get("preferences", {}).items():

        if key.replace("_"," ") in text or "music" in text:

            results.setdefault(
                "preferences",
                {}
            )

            results["preferences"][key] = value


    # goals

    if "goal" in text or "plan" in text:

        results["goals"] = memory.get(
            "goals",
            []
        )


    # user profile always

    results["user_profile"] = memory.get(
        "user_profile",
        {}
    )


    return results
