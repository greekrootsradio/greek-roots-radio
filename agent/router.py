from agent.memory import save_memory


def route(user_input, memory):

    text = user_input.lower().strip()

    # -------------------------
    # MEMORY STATUS
    # -------------------------
    if "memory" in text:
        count = len(memory.get("conversation_history", []))
        return f"I currently remember {count} conversations."

    # -------------------------
    # REMEMBER NAME
    # -------------------------
    if "my name is" in text:

        idx = text.find("my name is")
        name = user_input[idx + len("my name is"):].strip()

        if name:
            memory.setdefault("user_profile", {})
            memory["user_profile"]["name"] = name
            save_memory(memory)
            return f"Nice to meet you {name}. I will remember your name."

    # -------------------------
    # WHAT IS MY NAME
    # -------------------------
    if "what is my name" in text:

        name = memory.get("user_profile", {}).get("name")

        if name:
            return f"Your name is {name}."
        else:
            return "I don't know your name yet."

    # -------------------------
    # PROJECT MEMORY
    # -------------------------
    if "my project is" in text:

        idx = text.find("my project is")
        project = user_input[idx + len("my project is"):].strip()

        if project:
            memory.setdefault("projects", {})
            memory["projects"]["current"] = project
            save_memory(memory)
            return f"I have saved your project: {project}"

    return None
