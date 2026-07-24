class MemoryExtractor:


    def extract(self, user_input):

        memories = []

        text = user_input.lower()


        # -------------------------
        # NAME EXTRACTION
        # -------------------------
        if "my name is" in text:

            name = (
                user_input
                .split("is", 1)[1]
                .strip()
            )

            memories.append(
                {
                    "type": "user_profile",
                    "key": "name",
                    "value": name
                }
            )


        # -------------------------
        # PREFERENCE EXTRACTION
        # -------------------------
        if "i like" in text:

            preference = (
                user_input
                .lower()
                .split("i like", 1)[1]
                .strip()
            )

            memories.append(
                {
                    "type": "preference",
                    "value": preference
                }
            )


        return memories
