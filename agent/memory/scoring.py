from datetime import datetime


class MemoryScoring:


    def __init__(self):

        self.permanent_categories = [

            "user_profile",
            "family",
            "health",
            "important_dates",
            "preferences",
            "projects",
            "goals"

        ]


        self.temporary_categories = [

            "conversation",
            "weather",
            "short_term",
            "current_task"

        ]



    def score(self, memory):

        category = memory.get(
            "category",
            "conversation"
        )


        importance = 3


        if category in self.permanent_categories:

            importance = 10


        elif category in self.temporary_categories:

            importance = 2


        elif category == "preference":

            importance = 7


        elif category == "project":

            importance = 9



        memory["importance"] = importance


        memory["confidence"] = memory.get(
            "confidence",
            1.0
        )


        memory["permanent"] = (
            category in self.permanent_categories
        )


        memory["scored_at"] = str(
            datetime.now()
        )


        return memory




    def should_keep(self, memory):

        if memory.get(
            "permanent",
            False
        ):

            return True


        if memory.get(
            "importance",
            0
        ) >= 5:

            return True


        return False




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

                "update_required": True,

                "old": old_memory,

                "new": new_memory

            }


        return {

            "update_required": False

        }
