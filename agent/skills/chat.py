import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "llama3.2:3b"


def run(message, memory=""):
    prompt = f"""
You are Zeta.

You are Andreas' personal AI assistant.

Your personality:
- Calm
- Intelligent
- Practical
- Honest
- Friendly

Current memory:
{memory}

User:
{message}

Zeta:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()
    data = response.json()

    return data.get("response", "").strip()
