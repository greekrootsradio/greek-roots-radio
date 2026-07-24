import json
from agent.memory.storage import MemoryStorage


class MemoryRecall:

    def __init__(self):

        self.storage = MemoryStorage()


    def search(self, keyword):

        memories = self.storage.load()

        results = []

        for item in memories:

            text = json.dumps(
                item
            ).lower()

            if keyword.lower() in text:
                results.append(item)

        return results
