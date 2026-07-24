import requests

from agent.router import route
from agent.memory import save_memory
from agent.memory.recall import MemoryRecall


OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "llama3.2:3b"


def ask_ai(user_input, memory):

    # -------------------------
    # ROUTER FIRST
    # -------------------------
    routed = route(user_input, memory)

    if routed is not None:
        return routed


    # -------------------------
    # MEMORY RECALL
    # -------------------------
    recall = MemoryRecall()

    recalled_memories = recall.search(
        user_input
    )


    # -------------------------
    # BUILD MEMORY CONTEXT
    # -------------------------
    memory_context = {
        "user_profile": memory.get("user_profile", {}),
        "preferences": memory.get("preferences", {}),
        "projects": memory.get("projects", {}),
        "goals": memory.get("goals", []),
        "notes": memory.get("notes", []),
        "knowledge": memory.get("knowledge", {})
    }


    # -------------------------
    # AI FALLBACK
    # -------------------------
    prompt = f"""
You are Zeta, an autonomous personal AI assistant.

Your memory about the user:

{memory_context}

Relevant recalled memories:

{recalled_memories}

Conversation:

User:
{user_input}

Instructions:
- Be helpful and natural.
- Remember important facts about the user.
- Give concise but useful answers.
"""


    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )


    data = response.json()

    reply = data.get(
        "response",
        "I was unable to generate a response."
    )


    # -------------------------
    # STORE CONVERSATION MEMORY
    # -------------------------
    memory.setdefault(
        "conversation_history",
        []
    )


    memory["conversation_history"].append(
        {
            "user": user_input,
            "assistant": reply
        }
    )


    # Keep last 100 conversations
    memory["conversation_history"] = (
        memory["conversation_history"][-100:]
    )


    save_memory(memory)


    return reply
