import requests

from agent.router import route
from agent.memory import save_memory
from agent.memory.extractor import MemoryExtractor
from agent.memory.recall import MemoryRecall
from agent.memory.schema import create_memory
from agent.memory.consolidator import MemoryConsolidator


OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "llama3.2:3b"


extractor = MemoryExtractor()
recaller = MemoryRecall()
consolidator = MemoryConsolidator()


def ask_ai(user_input, memory):


    # -------------------------
    # ROUTER FIRST
    # -------------------------

    routed = route(
        user_input,
        memory
    )

    if routed is not None:
        return routed



    # -------------------------
    # EXTRACT NEW MEMORIES
    # -------------------------

    extracted = extractor.extract(
        user_input
    )


    schema_memories = []


    for item in extracted:


        if item["type"] == "user_profile":

            schema_memories.append(
                create_memory(
                    category="user_profile",
                    key=item["key"],
                    value=item["value"],
                    importance=10
                )
            )


        elif item["type"] == "preference":

            schema_memories.append(
                create_memory(
                    category="preference",
                    key="preference",
                    value=item["value"],
                    importance=5
                )
            )



    if schema_memories:

        memory["new_memories"] = schema_memories


        profile = consolidator.merge(
            schema_memories
        )


        memory.update(
            profile
        )



    # -------------------------
    # RECALL EXISTING MEMORY
    # -------------------------

    recall = recaller.search(
        user_input
    )


    memory["recall"] = recall



    # -------------------------
    # BUILD KNOWN FACTS
    # -------------------------

    known_facts = ""


    for item in recall:

        if isinstance(item, dict):

            if (
                "key" in item
                and "value" in item
            ):

                known_facts += (
                    f"{item['key']}: "
                    f"{item['value']}\n"
                )



    # -------------------------
    # BUILD MEMORY CONTEXT
    # -------------------------

    memory_context = {

        "user_profile":
            memory.get(
                "user_profile",
                {}
            ),

        "preferences":
            memory.get(
                "preferences",
                []
            ),

        "projects":
            memory.get(
                "projects",
                {}
            ),

        "goals":
            memory.get(
                "goals",
                []
            ),

        "notes":
            memory.get(
                "notes",
                []
            ),

        "knowledge":
            memory.get(
                "knowledge",
                {})
    }



    # -------------------------
    # DIRECT MEMORY ANSWERS
    # -------------------------

    if (
        "name" in user_input.lower()
        and memory.get("user_profile", {}).get("name")
    ):

        return (
            f"Your name is "
            f"{memory['user_profile']['name']}."
        )



    # -------------------------
    # AI FALLBACK
    # -------------------------

    prompt = f"""

You are Zeta, an autonomous personal AI assistant.

Known facts about the user:

{known_facts}


Memory context:

{memory_context}


Conversation:

User:
{user_input}


Instructions:

- Use known facts when answering.
- Never claim you do not know something that exists in memory.
- Be helpful and natural.
- Remember important facts about the user.
- Keep answers concise.
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
    # STORE CONVERSATION
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


    memory["conversation_history"] = (
        memory["conversation_history"][-100:]
    )


    save_memory(
        memory
    )


    return reply
