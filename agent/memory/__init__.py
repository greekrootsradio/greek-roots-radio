from agent.memory.storage import MemoryStorage


_storage = MemoryStorage()


def save_memory(memory):

    return _storage.save(
        {
            "type": "conversation",
            "memory": memory
        }
    )


def load_memory():

    return _storage.load()
