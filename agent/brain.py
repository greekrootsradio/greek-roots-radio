import json
import requests
from agent.router import route

MEMORY_FILE = "data/memory.json"

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "llama3.2:3b"


def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


def ask_ai(user_input, memory):
    # ---- ROUTER FIRST ----
    routed = route(user_input, memory)
    if routed is not None:
        return routed

    # ---- AI FALLBACK ----
    prompt = f"""
You are Zeta, an autonomous assistant.

Memory:
{memory}

User: {user_input}
Respond clearly and naturally.
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
    reply = data.get("response", "No response")

    memory[user_input] = reply
    save_memory(memory)

    return reply
