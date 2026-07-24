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
            "project",
            "goals"

        ]


    def score(self, memory):

        category = memory.get(
            "category",
            ""
        )

        key = memory.get(
            "key",
            ""
        )

        value = memory.get(
            "value",
            ""
        )


        importance = 5

        permanent = False


        # -------------------------
        # PERMANENT MEMORY
        # -------------------------

        if category in self.permanent_categories:

            permanent = True


            if category == "user_profile":

                importance = 10


            elif category == "health":

                importance = 10


            elif category == "family":

                importance = 10


            elif category == "projects":

                importance = 9


            elif category == "project":

                importance = 9


            elif category == "goals":

                importance = 8


            elif category == "preferences":

                importance = 7


            else:

                importance = 6



        # -------------------------
        # TEMPORARY MEMORY
        # -------------------------

        else:

            importance = 2



        # -------------------------
        # KEYWORD BOOSTS
        # -------------------------

        important_words = [

            "name",
            "birthday",
            "doctor",
            "allergy",
            "medicine",
            "project",
            "goal",
            "home",
            "family"

        ]


        combined = (
            str(key) +
            " " +
            str(value)
        ).lower()



        for word in important_words:

            if word in combined:

                importance += 1



        # Cap score

        if importance > 10:

            importance = 10



        return {

            **memory,

            "importance": importance,

            "confidence": memory.get(
                "confidence",
                1.0
            ),

            "permanent": permanent,

            "scored_at": str(
                datetime.now()
            )

        }
