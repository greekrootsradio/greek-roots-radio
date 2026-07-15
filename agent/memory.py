import json
import os
from copy import deepcopy

MEMORY_FILE = "data/memory.json"

DEFAULT_MEMORY = {
    "user_profile": {},
    "preferences": {},
    "projects": {},
    "goals": [],
    "tasks": [],
    "notes": [],
    "knowledge": {},
    "conversation_history": []
}


def _ensure_memory_file():
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)

    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump(DEFAULT_MEMORY, f, indent=2)


def load_memory():
    _ensure_memory_file()

    with open(MEMORY_FILE, "r") as f:
        try:
            memory = json.load(f)
        except json.JSONDecodeError:
            memory = deepcopy(DEFAULT_MEMORY)

    updated = False

    for key, value in DEFAULT_MEMORY.items():
        if key not in memory:
            memory[key] = deepcopy(value)
            updated = True

    if updated:
        save_memory(memory)

    return memory


def save_memory(memory):
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


def update_memory(key, value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)


def get_memory():
    return load_memory()
