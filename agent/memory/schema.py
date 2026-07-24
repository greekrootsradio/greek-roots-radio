import uuid
from datetime import datetime


def create_memory(
    category,
    key,
    value,
    source="conversation",
    importance=5,
    confidence=1.0
):

    return {
        "id": str(uuid.uuid4()),

        "category": category,

        "key": key,

        "value": value,

        "source": source,

        "importance": importance,

        "confidence": confidence,

        "created": str(datetime.now())
    }
