from agent.memory.storage import MemoryStorage


storage = MemoryStorage()


storage.save({
    "type": "test",
    "text": "Hello ZETA"
})


memories = storage.load()


assert len(memories) > 0

assert memories[-1]["text"] == "Hello ZETA"


print("ZETA MEMORY TEST PASSED")
