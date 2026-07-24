import requests

from agent.router import route

from agent.memory import save_memory, load_memory

from agent.memory.extractor import MemoryExtractor

from agent.memory.schema import create_memory

from agent.memory.consolidator import MemoryConsolidator

from agent.memory.recall import MemoryRecall


OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

MODEL = "llama3.2:3b"



extractor = MemoryExtractor()

consolidator = MemoryConsolidator()

recall = MemoryRecall()



def process_memory(user_input):

    extracted = extractor.extract(
        user_input
    )


    schema_memories = []


    for item in extracted:

        if item["type"] == "user_profile":

            schema_memories.append(
                create_memory(
                    "user_profile",
                    item["key"],
                    item["value"],
                    importance=10
                )
            )


        elif item["type"] == "preference":

            schema_memories.append(
                create_memory(
                    "preference",
                    "interest",
                    item["value"],
                    importance=5
                )
            )


    if schema_memories:

        profile = consolidator.merge(
            schema_memories
        )


        save_memory(
            {
                "type": "structured_memory",
                "memory": schema_memories
            }
        )


        return profile


    return {}



def ask_ai(user_input, memory):


    # -------------------------
    # MEMORY LEARNING
    # -------------------------

    learned = process_memory(
        user_input
    )


    if learned:

        memory.update(
            learned
        )


    # -------------------------
    # RECALL EXISTING MEMORY
    # -------------------------

    remembered = recall.search(
        user_input
    )


    memory["recall"] = remembered



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
    # AI CONTEXT
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

        "recall":
            remembered
    }



    prompt = f"""

You are Zeta, an autonomous personal AI assistant.

Memory about Andreas:

{memory_context}


User:

{user_input}


Instructions:

- Be helpful.
- Use memory when relevant.
- Learn important facts.
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

        "Unable to respond."

    )



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
