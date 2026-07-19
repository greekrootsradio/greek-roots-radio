import re

from agent.memory.core import (
    get_memory,
    save_memory
)


def extract_memory(message):

    memory = get_memory()

    text = message.lower()


    # --------------------
    # NAME DETECTION
    # --------------------

    name_patterns = [
        r"my name is (.+)",
        r"i am (.+)"
    ]

    for pattern in name_patterns:

        match = re.search(
            pattern,
            message,
            re.IGNORECASE
        )

        if match:

            name = match.group(1).strip()

            memory["user_profile"]["name"] = name

            break



    # --------------------
    # PROJECT DETECTION
    # --------------------

    project_patterns = [
        r"my project is (.+)",
        r"project is (.+)",
        r"my second project is (.+)"
    ]

    for pattern in project_patterns:

        match = re.search(
            pattern,
            message,
            re.IGNORECASE
        )

        if match:

            project = match.group(1).strip()

            memory["projects"][project] = {
                "status": "active"
            }

            break



    # --------------------
    # MUSIC PREFERENCE
    # --------------------

    music_patterns = [
        r"my favourite music style is (.+)",
        r"my favorite music style is (.+)",
        r"i like (.+)",
        r"i love (.+)"
    ]


    for pattern in music_patterns:

        match = re.search(
            pattern,
            message,
            re.IGNORECASE
        )


        if match:

            style = match.group(1).strip()

            memory["preferences"]["music_style"] = style

            break



    # --------------------
    # GOAL DETECTION
    # --------------------

    goal_patterns = [
        r"my goal is (.+)",
        r"i want to (.+)",
        r"i want zeta to (.+)"
    ]


    for pattern in goal_patterns:

        match = re.search(
            pattern,
            message,
            re.IGNORECASE
        )


        if match:

            goal = match.group(1).strip()

            if goal not in memory["goals"]:

                memory["goals"].append(goal)

            break



    # --------------------
    # REMEMBER NOTES
    # --------------------

    if "remember that" in text:

        match = re.search(
            r"remember that (.+)",
            message,
            re.IGNORECASE
        )


        if match:

            note = match.group(1).strip()

            memory["notes"].append(note)



    save_memory(memory)
