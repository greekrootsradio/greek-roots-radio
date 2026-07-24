from agent.memory.extractor import MemoryExtractor
from agent.memory.schema import create_memory
from agent.memory.consolidator import MemoryConsolidator
from agent.memory.recall import MemoryRecall


print("Starting ZETA memory pipeline test")


# Step 1 - Extract memory
extractor = MemoryExtractor()

facts = extractor.extract(
    "My name is Andreas"
)

print("\nExtracted:")
print(facts)


# Step 2 - Convert to schema objects

memory_objects = []

for fact in facts:

    memory = create_memory(
        fact["type"],
        fact["key"],
        fact["value"],
        importance=10
    )

    memory_objects.append(memory)


print("\nSchema objects:")
print(memory_objects)


# Step 3 - Consolidate

consolidator = MemoryConsolidator()

profile = consolidator.merge(
    memory_objects
)


print("\nConsolidated profile:")
print(profile)


# Step 4 - Recall

recall = MemoryRecall()

results = recall.search(
    "Andreas"
)


print("\nRecall results:")
print(results)


# Validation

assert (
    profile["user_profile"]["name"]
    == "Andreas"
)


print(
    "\nZETA MEMORY PIPELINE TEST PASSED"
)
