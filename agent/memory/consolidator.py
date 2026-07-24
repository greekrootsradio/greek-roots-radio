PYTHONPATH=. python3 - <<'PY'

from agent.memory.consolidator import MemoryConsolidator

c = MemoryConsolidator()

print(
    c.consolidate(
        [
            {
            "type":"user_profile",
            "key":"name",
            "value":"Andreas"
            },
            {
            "type":"preference",
            "value":"greek music"
            }
        ]
    )
)

PY
