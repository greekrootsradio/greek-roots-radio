import requests

from agent.memory import (
    get_memory,
    extract_memory,
    add_conversation
)

from agent.memory.recall import recall_memory


OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "llama3.2:3b"


def run(message):

    # Learn from Andreas
    extract_memory(message)

    # Load memory
    memory = get_memory()

    # Recall relevant memories
    recalled = recall_memory(message)


    prompt = f"""
You are ZETA.

You are Andreas Jackson's personal AI assistant.

You are running locally on Andreas' Mac Studio.

Personality:
- Calm
- Intelligent
- Practical
- Honest
- Friendly

Your purpose:
- Help Andreas build software
- Manage projects
- Assist with Greek Roots Radio
- Help with planning and technical tasks
- Become more autonomous over time

Known information about Andreas:

{recalled}


Current conversation:

Andreas:
{message}

Respond naturally. Use your memory when relevant.
"""


    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )


    result = response.json()["response"]


    add_conversation(
        message,
        result
    )


    return result
