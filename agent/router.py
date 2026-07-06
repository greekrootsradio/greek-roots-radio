def route(user_input, memory):
    text = user_input.lower()

    # ---- SYSTEM COMMANDS ----
    if "status" in text:
        return "Zeta is running autonomously in SAFE mode."

    if "memory" in text:
        return f"I currently store {len(memory)} entries."

    if "who are you" in text:
        return "I am Zeta, your autonomous local AI agent."

    # ---- SIMPLE INTELLIGENCE LAYER ----
    if "my name is" in text:
        name = user_input.split("is")[-1].strip()
        memory["name"] = name
        return f"Nice to meet you, {name}."

    # ---- DEFAULT ----
    return None
