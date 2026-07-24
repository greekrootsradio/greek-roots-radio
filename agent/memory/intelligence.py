from datetime import datetime


class MemoryIntelligence:


    def score_importance(self, memory):

        category = memory.get(
            "category",
            ""
        )


        if category == "user_profile":
            return 10


        if category == "project":
            return 9


        if category == "preference":
            return 5


        if category == "goal":
            return 8


        return 3



    def enrich(self, memory):

        memory["importance"] = self.score_importance(
            memory
        )

        memory["confidence"] = 1.0

        memory["updated"] = str(
            datetime.now()
        )

        return memory



    def compare(self, old_memory, new_memory):

        if (
            old_memory.get("key")
            ==
            new_memory.get("key")
            and
            old_memory.get("category")
            ==
            new_memory.get("category")
        ):

            return {
                "conflict": True,
                "old": old_memory,
                "new": new_memory
            }


        return {
            "conflict": False
        }
